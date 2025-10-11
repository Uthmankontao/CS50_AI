import csv
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    load_data(sys.argv[1])
    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # raise NotImplementedError

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        # data = []
        # for row in reader:
        #     data.append({
        #     "evidence": row[:17],
        #     "label": 1 if row[-1] == "TRUE" else 0
        # })
        # months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        # evidence, labels = [], []
        # for _ in range(len(data)):
        #     for i in [1, 3, 5, 6, 7, 8, 9]:
        #         data[_]["evidence"][i] = float(data[_]["evidence"][i])
        #     if data[_]["evidence"][10] in months:
        #         data[_]["evidence"][10] = int(months.index(data[_]["evidence"][10]))
        #     else:
        #         continue
        #     if data[_]["evidence"][-2] == "Returning_Visitor":
        #         data[_]["evidence"][-2] = 1
        #     else:
        #         data[_]["evidence"][-2] = 0
        #     if data[_]["evidence"][-1] == "TRUE":
        #         data[_]["evidence"][-1] = 1
        #     else: 
        #         data[_]["evidence"][-1] = 0
        #     evidence.append(data[_]["evidence"])
        #     labels.append(data[_]["label"])
        months = {
        'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3,
        'May': 4, 'June': 5, 'Jul': 6, 'Aug': 7,
        'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11
        }
        evidence, labels = [], []
        for row in reader:
            sample = [
                int(row[0]),                        # Administrative
                float(row[1]),                      # Administrative_Duration
                int(row[2]),                        # Informational
                float(row[3]),                      # Informational_Duration
                int(row[4]),                        # ProductRelated
                float(row[5]),                      # ProductRelated_Duration
                float(row[6]),                      # BounceRates
                float(row[7]),                      # ExitRates
                float(row[8]),                      # PageValues
                float(row[9]),                      # SpecialDay
                months[row[10]],                    # Month
                int(row[11]),                       # OperatingSystems
                int(row[12]),                       # Browser
                int(row[13]),                       # Region
                int(row[14]),                       # TrafficType
                1 if row[15] == "Returning_Visitor" else 0,  # VisitorType
                1 if row[16] == "TRUE" else 0       # Weekend
            ]
            evidence.append(sample)
            labels.append(1 if row[17] == "TRUE" else 0)
        return (evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    # raise NotImplementedError
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model



def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    # raise NotImplementedError
    true_positive = 0
    false_negative = 0
    true_negative = 0
    false_positive = 0

    for actual, predicted in zip(labels, predictions):
        if actual == 1:
            if predicted == 1:
                true_positive += 1
            else:
                false_negative += 1
        else: 
            if predicted == 0:
                true_negative += 1
            else:
                false_positive += 1

    sensitivity = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0
    specificity = true_negative / (true_negative + false_positive) if (true_negative + false_positive) > 0 else 0
    return (sensitivity, specificity)



if __name__ == "__main__":
    main()
