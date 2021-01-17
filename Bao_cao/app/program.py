import processing_data
import pickle


def pre(text):
    text = processing_data.text_preprocess(text)
    with open('tfidf.pickle', 'rb') as f:
        tfidf = pickle.load(f)
    with open('model.pickle', 'rb') as f:
        model = pickle.load(f)

    category_codes = {0: 'đời sống',
                      1: 'giải trí',
                      2: 'giáo dục',
                      3: 'kinh doanh',
                      4: 'pháp luật',
                      5: 'sức khỏe',
                      6: 'others'}


    features = tfidf.transform([text]).toarray()

    predict = model.predict(features)[0]
    proba = int(model.predict_proba(features)[0][predict] * 100)

    if proba <= 50:
        predict = 6
    return category_codes[predict], proba


if __name__ == '__main__':
    pass
