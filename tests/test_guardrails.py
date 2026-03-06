import pytest
from app.services.guardrails_service import validate_response


def test_valid_llm_response():

    response = """
    {
      "claim_type": "vehicle_damage",
      "risk_score": 0.25,
      "explanation": "Vehicle damage claim detected"
    }
    """

    data = validate_response(response)

    assert data["claim_type"] == "vehicle_damage"
    assert "risk_score" in data


def test_invalid_response():

    response = "This is not JSON"

    with pytest.raises(ValueError):
        validate_response(response)
