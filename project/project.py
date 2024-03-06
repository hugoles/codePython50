import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class AnimeReviewScraper:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.total_reviews = 0
        self.correct_estimatives = 0

    def scrape_reviews(self, n_pages):
        for n_page in range(n_pages):
            url = f'https://myanimelist.net/reviews.php?t=anime&filter_check=&filter_hide=&preliminary=on&spoiler=off&p={n_page}'
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                review_elements = soup.find_all(class_='review-element js-review-element')

                for review in review_elements:
                    anime_title = review.find(class_='title ga-click').text.strip()
                    rating_element = review.find(class_='rating mt20 mb20 js-hidden')
                    numerical_rating = int(rating_element.find(class_='num').text.strip())
                    review_text = review.find(class_='text').text.strip()

                    sentiment_score = self.analyzer.polarity_scores(review_text)
                    sentiment_label = self._get_sentiment_label(sentiment_score['compound'])
                    verification_result = self.verify_estimative(sentiment_label, numerical_rating)

                    self.total_reviews += 1
                    if verification_result == 'Correct':
                        self.correct_estimatives += 1

                    self._print_review_info(anime_title, numerical_rating, review_text, sentiment_label, verification_result)

            else:
                print(f'Failed to retrieve the page. Status code: {response.status_code}')

    def _get_sentiment_label(self, compound_score):
        if compound_score >= 0.05:
            return 'Positive'
        elif compound_score <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    def verify_estimative(self, sentiment_label, numerical_rating):
        if 6 <= numerical_rating <= 10 and sentiment_label == 'Positive':
            return 'Correct'
        elif numerical_rating == 5 and sentiment_label == 'Neutral':
            return 'Correct'
        elif 0 <= numerical_rating <= 4 and sentiment_label == 'Negative':
            return 'Correct'
        else:
            return 'Incorrect'

    def accuracy_percentage(self):
        if self.total_reviews == 0:
            return 0
        return (self.correct_estimatives / self.total_reviews) * 100

    def _print_review_info(self, anime_title, numerical_rating, review_text, sentiment_label, verification_result):
        print(f'{"="*50}')
        print(f'Anime: {anime_title}')
        print(f'Rating: {numerical_rating}')
        print(f'Review: {review_text}')
        print(f'Sentiment: {sentiment_label}')
        print(f'Estimative Verification: {verification_result}\n')

def main():
    n_pages = int(input('Enter the number of pages: '))
    scraper = AnimeReviewScraper()
    scraper.scrape_reviews(n_pages)
    accuracy = scraper.accuracy_percentage()
    print(f'Accuracy of sentiment estimative: {accuracy:.2f}%')

if __name__ == '__main__':
    main()
