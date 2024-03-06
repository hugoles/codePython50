from project import get_sentiment_label, verify_estimative, accuracy_percentage

def test_get_sentiment_label():
    # Test cases for get_sentiment_label
    # Positive compound score
    assert get_sentiment_label(0.1) == 'Positive'

    # Negative compound score
    assert get_sentiment_label(-0.1) == 'Negative'

    # Neutral compound score
    assert get_sentiment_label(0.03) == 'Neutral'


def test_verify_estimative():
    # Test cases for verify_estimative
    # Correct estimative for positive sentiment and rating 8
    assert verify_estimative('Positive', 8) == 'Correct'

    # Incorrect estimative for negative sentiment and rating 8
    assert verify_estimative('Negative', 8) == 'Incorrect'


def test_accuracy_percentage():
    # Test case for accuracy_percentage
    assert accuracy_percentage(100, 70) == 70.0
