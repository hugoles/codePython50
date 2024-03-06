import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Get the reviews
def scrape_reviews(n_pages):
    total_reviews = 0
    correct_estimatives = 0
    reviews = []

    for n_page in range(1, n_pages + 1):
        url = f'https://myanimelist.net/reviews.php?t=anime&filter_check=&filter_hide=&preliminary=on&spoiler=off&p={n_page}'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            review_elements = soup.find_all(class_='review-element js-review-element')
            reviews.extend(review_elements)

            # Update total_reviews for each review scraped
            total_reviews += len(review_elements)

            # Update correct_estimatives for each review
            for review in review_elements:
                anime_title = review.find(class_='title ga-click').text.strip()
                rating_element = review.find(class_='rating mt20 mb20 js-hidden')
                numerical_rating = int(rating_element.find(class_='num').text.strip())
                review_text = review.find(class_='text').text.strip()

                analyzer = SentimentIntensityAnalyzer()
                sentiment_score = analyzer.polarity_scores(review_text)
                sentiment_label = get_sentiment_label(sentiment_score['compound'])
                verification_result = verify_estimative(sentiment_label, numerical_rating)

                if verification_result == 'Correct':
                    correct_estimatives += 1

        else:
            print(f'Failed to retrieve the page. Status code: {response.status_code}')

    return reviews, total_reviews, correct_estimatives

# Get the sentiment estimative
def get_sentiment_label(compound_score):
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Verify if it is correct
def verify_estimative(sentiment_label, numerical_rating):
    if 6 <= numerical_rating <= 10 and sentiment_label == 'Positive':
        return 'Correct'
    elif numerical_rating == 5 and sentiment_label == 'Neutral':
        return 'Correct'
    elif 0 <= numerical_rating <= 4 and sentiment_label == 'Negative':
        return 'Correct'
    else:
        return 'Incorrect'

# The percentage of accuracy
def accuracy_percentage(total_reviews, correct_estimatives):
    if total_reviews == 0:
        return 0
    return (correct_estimatives / total_reviews) * 100

'''
# test
def print_review_info(anime_title, numerical_rating, review_text, sentiment_label, verification_result):
    print(f'{"="*50}')
    print(f'Anime: {anime_title}')
    print(f'Rating: {numerical_rating}')
    print(f'Review: {review_text}')
    print(f'Sentiment: {sentiment_label}')
    print(f'Estimative Verification: {verification_result}\n')
'''

# Get the sentiment estimative for a one anime title
def sentiment_estimative_for_anime_title(anime_title, reviews):
    anime_reviews = []
    for review in reviews:
        review_anime_title = review.find(class_='title ga-click').text.strip()
        if anime_title.lower() in review_anime_title.lower():
            review_text = review.find(class_='text').text.strip()
            analyzer = SentimentIntensityAnalyzer()
            sentiment_score = analyzer.polarity_scores(review_text)
            sentiment_label = get_sentiment_label(sentiment_score['compound'])
            anime_reviews.append((review_anime_title, sentiment_label))
    return anime_reviews


# Get the biggest rating review
def find_biggest_rating_review(reviews):
    biggest_rating = 0
    biggest_rating_review = ""
    for review in reviews:
        rating_element = review.find(class_='rating mt20 mb20 js-hidden')
        numerical_rating = int(rating_element.find(class_='num').text.strip())
        if numerical_rating > biggest_rating:
            biggest_rating = numerical_rating
            biggest_rating_review = review.find(class_='text').text.strip()
    return biggest_rating, biggest_rating_review

# Get the smallest rating review
def find_smallest_rating_review(reviews):
    smallest_rating = float('inf')
    smallest_rating_review = ""
    for review in reviews:
        rating_element = review.find(class_='rating mt20 mb20 js-hidden')
        numerical_rating = int(rating_element.find(class_='num').text.strip())
        if numerical_rating < smallest_rating:
            smallest_rating = numerical_rating
            smallest_rating_review = review.find(class_='text').text.strip()
    return smallest_rating, smallest_rating_review

def main():
    # Ask for the number of pages to scrape
    while True:
        try:
            n_pages = int(input('Enter the number of pages to scrape (maximum 3): '))
            if n_pages <= 0:
                print("Number of pages must be a positive integer. Please try again.")
            elif n_pages > 3:
                print("Number of pages cannot exceed 3. Setting it to 3.")
                n_pages = 3
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    reviews, total_reviews, correct_estimatives = scrape_reviews(n_pages)

    while True:
        print("\n" + "="*52)
        print("||" + " "*25 + "MENU" + " "*25 + "||")
        print("="*52)
        print("||  1. Get sentiment estimative for an anime title      ||")
        print("||  2. Get accuracy percentage of sentiment estimative  ||")
        print("||  3. Get biggest and smallest review                  ||")
        print("||  4. Exit                                             ||")
        print("="*52)

        choice = input("Enter your choice: ")

        if choice == '1':
            anime_title = input("Enter the anime title: ")
            anime_reviews = sentiment_estimative_for_anime_title(anime_title, reviews)
            if anime_reviews:
                print(f'Sentiment Estimatives for "{anime_title}":')
                for review in anime_reviews:
                    print(f'Anime: {review[0]}, Sentiment: {review[1]}')
            else:
                print(f'No reviews found for "{anime_title}".')

        elif choice == '2':
            accuracy = accuracy_percentage(total_reviews, correct_estimatives)
            print(f'Accuracy of sentiment estimative: {accuracy:.2f}%')

        elif choice == '3':
            biggest_rating, biggest_rating_review = find_biggest_rating_review(reviews)
            smallest_rating, smallest_rating_review = find_smallest_rating_review(reviews)
            print(f'\nReview with the Biggest Rating ({biggest_rating}):')
            print(biggest_rating_review)
            print(f'\nReview with the Smallest Rating ({smallest_rating}):')
            print(smallest_rating_review)

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    main()
