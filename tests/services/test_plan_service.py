import pytest;
from services.plan_service import PlanService;
from repositories.plan_repository import PlanRepository;


def test_plan_get_all(mocker):
    mock_repo = mocker.Mock(spec = PlanRepository);
    mock_repo.get_all.return_value = {"id":1,"name":"Basic Plan"};
    service = PlanService(mock_repo);
    data = service.get_all();
    assert data == {"id":1,"name":"Basic Plan"};

def test_plan_add(mocker):
    mock_repo = mocker.Mock(spec = PlanRepository);
    mock_repo.save.return_value = [1,3];
    service = PlanService(mock_repo);
    data = service.add("Basic",60,600,"This is test des");
    assert data == [1,3];



    