from flask import Flask, jsonify, request

app = Flask(__name__)

# Пример базы данных пользователей и постов
users = [
    {"id": 1, "username": "user1", "email": "user1@example.com", "password": "password1"},
    {"id": 2, "username": "user2", "email": "user2@example.com", "password": "password2"}
]
posts = [
    {"id": 1, "title": "Post 1", "content": "Content of post 1", "author_id": 1},
    {"id": 2, "title": "Post 2", "content": "Content of post 2", "author_id": 2}
]

# Роуты для постов
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return jsonify(post)
    return jsonify({"message": "Post not found"}), 404

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    new_post = {
        "id": len(posts) + 1,
        "title": data['title'],
        "content": data['content'],
        "author_id": data['author_id']
    }
    posts.append(new_post)
    return jsonify(new_post), 201

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        data = request.json
        post.update(data)
        return jsonify(post)
    return jsonify({"message": "Post not found"}), 404

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        posts.remove(post)
        return jsonify({"message": "Post deleted"})
    return jsonify({"message": "Post not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
