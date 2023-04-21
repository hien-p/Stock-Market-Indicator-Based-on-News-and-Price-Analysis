# from NewsInputPipe import prepare_bert_tf_input
from NewsModelPipe import infer_tf_news
print("Testing")


def test_input():
    ds = prepare_bert_tf_input('./sample.csv','title','label')
    print(ds)

def test_model():
    path = 'mlflow-artifacts:/7c1e386451f94b5482fe1a32cabb0474/3b2a1530cd8145328a08b4b24cb1e58b/artifacts/bert_cross_cookie_milk'
    infer_tf_news('',path)

test_model()