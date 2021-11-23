import pytest
from pysentimiento import create_analyzer



@pytest.fixture
def analyzer_es():
    return create_analyzer(task="hate_speech", lang="es")

@pytest.fixture
def analyzer_en():
    return create_analyzer(task="hate_speech", lang="en")

def test_not_hateful(analyzer_es):
    assert analyzer_es.predict("Qué buena onda!!!!").output == []


def test_hateful(analyzer_es):
    assert "hateful" in analyzer_es.predict("Odio a todos los putos negros de mierda!").output