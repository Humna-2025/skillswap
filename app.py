from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import bcrypt
import sys

app = Flask(__name__)
CORS(app)

print("=" * 50)
print("Starting SkillSwap Backend...")
print("=" * 50)

# MongoDB Connection
try:
    client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
    db = client['skillswap_db']
    users = db['users']
    swap_requests = db['swap_requests']
    transactions = db['transactions']
    ratings = db['ratings']
    
    # Test connection
    client.admin.command('ping')
    print("✅ Connected to MongoDB successfully!")
    print(f"   Database: skillswap_db")
    print(f"   Collections: {db.list_collection_names()}")
except Exception as e:
    print(f"❌ MongoDB Connection Error: {e}")
    print("   Please make sure MongoDB is running on localhost:27017")
    sys.exit(1)

# Test endpoint
@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"message": "SkillSwap API is running!", "status": "ok"}), 200

# ==================== AUTHENTICATION ENDPOINTS ====================

@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.json
        print(f"Register attempt: {data['email']}")
        
        # Check if user exists
        existing_user = users.find_one({"email": data['email']})
        if existing_user:
            return jsonify({"error": "Email already exists"}), 400
        
        # Generate user_id
        user_count = users.count_documents({})
        user_id = f"USR{user_count + 1:03d}"
        
        # IMPORTANT: Store password as plain text for demo (not hashed)
        # This matches your sample data
        user = {
            "user_id": user_id,
            "name": data['name'],
            "email": data['email'],
            "password": data['password'],  # Plain text password
            "department": data.get('department', ''),
            "credits": 10,
            "skills_offer": [],
            "skills_want": [],
            "rating_avg": 0,
            "total_swaps": 0,
            "bio": "",
            "experience_level": "Beginner",
            "availability": "Flexible",
            "created_at": datetime.now().isoformat()
        }
        
        users.insert_one(user)
        print(f"✅ New user registered: {user['name']} ({user_id})")
        return jsonify({"message": "User created successfully", "user_id": user_id}), 201
    except Exception as e:
        print(f"Error in register: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.json
        print(f"Login attempt: {data['email']}")
        
        # Find user by email
        user = users.find_one({"email": data['email']})
        
        if not user:
            print(f"❌ User not found: {data['email']}")
            return jsonify({"error": "User not found"}), 404
        
        # SIMPLE PASSWORD COMPARISON (plain text)
        # Since sample data has plain text passwords, we compare directly
        if data['password'] == user.get('password', ''):
            print(f"✅ Login successful: {user['name']}")
            return jsonify({
                "message": "Login successful",
                "user": {
                    "user_id": user['user_id'],
                    "name": user['name'],
                    "email": user['email'],
                    "credits": user.get('credits', 10),
                    "skills_offer": user.get('skills_offer', []),
                    "skills_want": user.get('skills_want', []),
                    "department": user.get('department', ''),
                    "rating_avg": user.get('rating_avg', 0),
                    "total_swaps": user.get('total_swaps', 0),
                    "bio": user.get('bio', ''),
                    "experience_level": user.get('experience_level', 'Beginner'),
                    "availability": user.get('availability', 'Flexible')
                }
            }), 200
        else:
            print(f"❌ Login failed: Invalid password for {data['email']}")
            return jsonify({"error": "Invalid password"}), 401
    except Exception as e:
        print(f"Error in login: {e}")
        return jsonify({"error": str(e)}), 500

# ==================== USER ENDPOINTS ====================

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        all_users = list(users.find({}, {"password": 0}))
        for user in all_users:
            user['_id'] = str(user['_id'])
        return jsonify(all_users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = users.find_one({"user_id": user_id}, {"password": 0})
        if user:
            user['_id'] = str(user['_id'])
            return jsonify(user), 200
        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.json
        update_data = {}
        
        if 'skills_offer' in data:
            update_data['skills_offer'] = data['skills_offer']
        if 'skills_want' in data:
            update_data['skills_want'] = data['skills_want']
        if 'bio' in data:
            update_data['bio'] = data['bio']
        if 'experience_level' in data:
            update_data['experience_level'] = data['experience_level']
        if 'availability' in data:
            update_data['availability'] = data['availability']
        
        result = users.update_one({"user_id": user_id}, {"$set": update_data})
        if result.modified_count > 0:
            return jsonify({"message": "User updated successfully"}), 200
        return jsonify({"error": "User not found or no changes"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== SEARCH ENDPOINTS ====================

@app.route('/api/search', methods=['GET'])
def search():
    try:
        skill = request.args.get('skill', '')
        category = request.args.get('category', '')
        experience = request.args.get('experience', '')
        
        query = {}
        if skill:
            query["skills_offer"] = {"$regex": skill, "$options": "i"}
        if category and category != "All Categories":
            query["skills_offer"] = {"$regex": category, "$options": "i"}
        if experience and experience != "All Levels":
            query["experience_level"] = experience
        
        results = list(users.find(query, {"password": 0}))
        for result in results:
            result['_id'] = str(result['_id'])
        
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/search/by-skill/<skill_name>', methods=['GET'])
def search_by_skill(skill_name):
    try:
        results = list(users.find(
            {"skills_offer": {"$regex": skill_name, "$options": "i"}},
            {"password": 0}
        ))
        for result in results:
            result['_id'] = str(result['_id'])
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== SWAP REQUEST ENDPOINTS ====================

@app.route('/api/swap-request', methods=['POST'])
def create_swap_request():
    try:
        data = request.json
        request_count = swap_requests.count_documents({})
        request_id = f"SWP{request_count + 1:03d}"
        
        swap = {
            "request_id": request_id,
            "requester_id": data['requester_id'],
            "requester_name": data['requester_name'],
            "receiver_id": data['receiver_id'],
            "receiver_name": data['receiver_name'],
            "skill_offered": data['skill_offered'],
            "skill_requested": data['skill_requested'],
            "credits_proposed": data['credits_proposed'],
            "status": "pending",
            "message": data.get('message', ''),
            "created_at": datetime.now().isoformat(),
            "responded_at": None,
            "completed_at": None
        }
        
        swap_requests.insert_one(swap)
        print(f"✅ Swap request created: {request_id}")
        return jsonify({
            "message": "Swap request sent successfully",
            "request_id": request_id
        }), 201
    except Exception as e:
        print(f"Error creating swap request: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/swap-requests/<user_id>', methods=['GET'])
def get_user_swap_requests(user_id):
    try:
        requests = list(swap_requests.find({
            "$or": [
                {"requester_id": user_id},
                {"receiver_id": user_id}
            ]
        }))
        
        for req in requests:
            req['_id'] = str(req['_id'])
        
        return jsonify(requests), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/swap-request/<request_id>/accept', methods=['PUT'])
def accept_swap_request(request_id):
    try:
        result = swap_requests.update_one(
            {"request_id": request_id},
            {"$set": {"status": "accepted", "responded_at": datetime.now().isoformat()}}
        )
        
        if result.modified_count > 0:
            return jsonify({"message": "Swap request accepted"}), 200
        return jsonify({"error": "Request not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/swap-request/<request_id>/decline', methods=['PUT'])
def decline_swap_request(request_id):
    try:
        result = swap_requests.update_one(
            {"request_id": request_id},
            {"$set": {"status": "declined", "responded_at": datetime.now().isoformat()}}
        )
        
        if result.modified_count > 0:
            return jsonify({"message": "Swap request declined"}), 200
        return jsonify({"error": "Request not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/swap-request/<request_id>/complete', methods=['PUT'])
def complete_swap(request_id):
    try:
        swap = swap_requests.find_one({"request_id": request_id})
        if not swap:
            return jsonify({"error": "Request not found"}), 404
        
        # Transfer credits
        teacher_id = swap['requester_id']
        learner_id = swap['receiver_id']
        credits = swap['credits_proposed']
        
        # Update credit balances
        users.update_one({"user_id": teacher_id}, {"$inc": {"credits": credits, "total_swaps": 1}})
        users.update_one({"user_id": learner_id}, {"$inc": {"credits": -credits, "total_swaps": 1}})
        
        # Create transaction record
        transaction_count = transactions.count_documents({})
        transaction = {
            "transaction_id": f"TXN{transaction_count + 1:03d}",
            "swap_request_id": request_id,
            "teacher_id": teacher_id,
            "learner_id": learner_id,
            "skill_taught": swap['skill_offered'],
            "credits_exchanged": credits,
            "status": "completed",
            "completed_at": datetime.now().isoformat()
        }
        transactions.insert_one(transaction)
        
        # Update swap request
        swap_requests.update_one(
            {"request_id": request_id},
            {"$set": {"status": "completed", "completed_at": datetime.now().isoformat()}}
        )
        
        # Get updated user for response
        teacher = users.find_one({"user_id": teacher_id}, {"password": 0})
        
        return jsonify({
            "message": "Swap completed, credits transferred",
            "teacher_credits": teacher['credits'] if teacher else 0
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== TRANSACTION ENDPOINTS ====================

@app.route('/api/transactions/<user_id>', methods=['GET'])
def get_transactions(user_id):
    try:
        user_transactions = list(transactions.find({
            "$or": [
                {"teacher_id": user_id},
                {"learner_id": user_id}
            ]
        }))
        
        for txn in user_transactions:
            txn['_id'] = str(txn['_id'])
        
        return jsonify(user_transactions), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== RATING ENDPOINTS ====================

@app.route('/api/rating', methods=['POST'])
def add_rating():
    try:
        data = request.json
        rating_count = ratings.count_documents({})
        rating_id = f"RAT{rating_count + 1:03d}"
        
        rating = {
            "rating_id": rating_id,
            "swap_request_id": data['swap_request_id'],
            "reviewer_id": data['reviewer_id'],
            "reviewed_id": data['reviewed_id'],
            "rating": data['rating'],
            "comment": data.get('comment', ''),
            "created_at": datetime.now().isoformat()
        }
        
        ratings.insert_one(rating)
        
        # Update user's average rating
        user_ratings = list(ratings.find({"reviewed_id": data['reviewed_id']}))
        if user_ratings:
            avg_rating = sum(r['rating'] for r in user_ratings) / len(user_ratings)
            users.update_one(
                {"user_id": data['reviewed_id']},
                {"$set": {"rating_avg": round(avg_rating, 1)}}
            )
        
        return jsonify({"message": "Rating submitted successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== LEADERBOARD ENDPOINTS ====================

@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    try:
        top_users = list(users.find(
            {},
            {"name": 1, "credits": 1, "rating_avg": 1, "total_swaps": 1, "skills_offer": 1, "_id": 0}
        ).sort([("credits", -1), ("rating_avg", -1)]).limit(10))
        
        for idx, user in enumerate(top_users, 1):
            user['rank'] = idx
            user['skills_count'] = len(user.get('skills_offer', []))
        
        return jsonify(top_users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== NOTIFICATION ENDPOINTS ====================

@app.route('/api/notifications/<user_id>', methods=['GET'])
def get_notifications(user_id):
    try:
        pending_requests = list(swap_requests.find({
            "receiver_id": user_id,
            "status": "pending"
        }))
        
        notifications = []
        for req in pending_requests:
            notifications.append({
                "id": req['request_id'],
                "type": "new_request",
                "message": f"{req['requester_name']} wants to learn {req['skill_requested']} from you",
                "data": req,
                "created_at": req['created_at']
            })
        
        return jsonify(notifications), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("=" * 50)
    print("Starting Flask server...")
    print("API will be available at: http://127.0.0.1:5000")
    print("Test endpoint: http://127.0.0.1:5000/api/test")
    print("=" * 50)
    app.run(debug=True, port=5000, host='127.0.0.1')