import pytest

@pytest.fixture
def mock_execution_context(mocker):
    mock_context = mocker.Mock()
    mock_context.parameters.database = "test_database"
    mock_context.parameters.model_version_id = 12345
    mock_context.parameters.add_csmr_cause = 173
    return mock_context
  
