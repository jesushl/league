# Target app
from urllib import response
from main import app
# Test libraty
from fastapi.testclient import TestClient


client = TestClient(app)
"""
This tests conusmes default values from matrix.csv
"""

def text_clear(text):
    """
    Clean text to validate only content and not format
    """
    text = text.replace(" ", "")
    text = text.replace("\n", "")
    return text


def test_echo():
    """
    This is a test about matrix representation return
    """
    response = client.get('/echo')
    assert response.status_code == 200
    assert text_clear(response.raw) == text_clear(
        """
        <table border="1" class="dataframe">
            <tbody>
                <tr>
                <td>1</td>
                <td>2</td>
                <td>3</td>
                </tr>
                <tr>
                <td>4</td>
                <td>5</td>
                <td>6</td>
                </tr>
                <tr>
                <td>7</td>
                <td>8</td>
                <td>9</td>
                </tr>
            </tbody>
        </table>
    """
    )

def test_invert():
    """
    This is a test about matrix representation return
    """
    response = client.get('/invert')
    assert response.status_code == 200
    assert text_clear(response.raw) == text_clear(
        """
        <table border="1" class="dataframe">
            <tbody>
                <tr>
                <td>1</td>
                <td>4</td>
                <td>7</td>
                </tr>
                <tr>
                <td>2</td>
                <td>5</td>
                <td>8</td>
                </tr>
                <tr>
                <td>3</td>
                <td>6</td>
                <td>9</td>
                </tr>
            </tbody>
        </table>

    """
    )


def test_flatten():
    """
    This is a test about matrix representation return
    """
    response = client.get('/flatten')
    assert response.status_code == 200
    assert text_clear(response.raw) == text_clear(
        """
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        """
    )


def test_sum():
    """
    This is a test about matrix representation return
    """
    response = client.get('/sum')
    assert response.status_code == 200
    assert response.raw ==  "45"


def test_multiply():
    """
    This is a test about matrix representation return
    """
    response = client.get('/sum')
    assert response.status_code == 200
    assert response.raw ==  "362880"