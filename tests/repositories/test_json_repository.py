import json;
import pytest;
from repositories.json_repository import JsonRepository;
from pathlib import Path;
from models.user import User;
@pytest.fixture
def repo(tmp_path,monkeypatch):
     monkeypatch.setattr(
        "constants.DEFAULT_SCHEMA_FOLDER",
        "db"
    )
     monkeypatch.chdir(tmp_path)

     return JsonRepository("users")
def test_repository_initialization(repo):
    assert repo.list == {
        "index": 1,
        "data": []
    }
    assert Path(repo.path).exists()

def test_add_user(repo):
    user = User("demo", "demo@gmail.com", "admin","Admin@123")

    result = repo.add(user)

    assert result.id == 1
    assert result.name == "demo"
    assert result.email == "demo@gmail.com"

def test_auto_incementing_id(repo):
    user = User("demo", "demo@gmail.com", "admin","Admin@123");
    user2 = User("demo2", "demo2@gmail.com", "admin","Admin@123");
    result = repo.add(user);
    result2 = repo.add(user2);

    assert result.id == 1;
    assert result2.id == 2;

def test_get_all(repo):
    user = User("demo", "demo@gmail.com", "admin","Admin@123");
    user2 = User("demo2", "demo2@gmail.com", "admin","Admin@123");
    repo.add(user);
    repo.add(user2);

    data = repo.get_all();
    assert len(data) == 2;
    assert data[0]['email'] == "demo@gmail.com";
    assert data[1]['email'] == "demo2@gmail.com";

def test_update(repo):
    user = User("demo", "demo@gmail.com", "admin","Admin@123");
    result_user = repo.add(user);

    data = repo.get_all();
    assert len(data) == 1;
    assert data[0]['email'] == "demo@gmail.com";

    result_user.email  = "test@gmail.com";
    repo.update(result_user);
    updated_data = repo.get_all();
    assert updated_data[0]['email'] == "test@gmail.com";

def test_remove(repo):
    user = User("demo", "demo@gmail.com", "admin","Admin@123");
    user2 = User("demo2", "demo2@gmail.com", "admin","Admin@123");
    repo.add(user);
    repo.add(user2);

    repo.remove(2);
    
    data = repo.get_all();
    assert len(data) == 1;

def test_get_by_id(repo):
    user = User("demo", "demo@gmail.com", "admin","Admin@123");
    user2 = User("demo2", "demo2@gmail.com", "admin","Admin@123");
    repo.add(user);
    repo.add(user2);

    data = repo.get_by_id(2);
    data['email'] == "demo2@gmail.com";


    


    

    