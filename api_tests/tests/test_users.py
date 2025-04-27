import pytest, requests, os


created_user_id = None


class Test_User_API:
    
    @pytest.fixture()
    def user_payload(self):
        return {
            "name": "John Doe",
            "email": "johndoe@gmail.com",
            "password": "password123"
        }
    def test_create_user(self, session, base_url, user_payload):
        global created_user_id
        self.payload = user_payload
        url = f"{base_url}/users"
        response = session.post(url, json=self.payload)
        assert response.status_code == 201
        body = response.json()
        assert body["name"] == self.payload["name"]
        assert id in body["id"]
        created_user_id = body["id"]
    

    @pytest.mark.dependency(depends=["test_create_user"])
    def test_get_user(self, session, base_url):
        global created_user_id
        url = f"{base_url}/users/{created_user_id}"
        response = session.get(url)
        assert response.status_code == 200
        body = response.json()
        assert body["id"] == created_user_id
        assert body["name"] == self.payload["name"]
        assert body["email"] == self.payload["email"]