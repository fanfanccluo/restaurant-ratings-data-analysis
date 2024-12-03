with open('./yelp_academic_dataset_review.json', 'r') as f:
    with open('./yelp_academic_dataset_review_1.json', 'a') as w:
        for i in range(100000):
            w.write(f.readline())
