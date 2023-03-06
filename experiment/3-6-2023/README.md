<h1>Report on NLP</h1>
<p>Begin on 19/2/2023 to 6/3/2023</p>
<h2>Structure</h2>
<p>The report is organized as follow:</p>
<ol>
    <li>Devops task</li>
    <li>Parameterized notebook</li>
    <li>Fine tune a BERT model</li>
</ol>
<h2>I. Devops task</h2>
<p>
    I was entrusted with learning devops which is mainly useful when deploying a model. And I'm glad to report that it's going well despite that model deploying haven't been done yet.
</p>
<h3><i>a. Problems</i></h3>
<p>Allow me to list some problems we had before:</p>
<ol>
    <li>We don't have a storage to store preprocessed data, models, versions, metadata...</li>
    <li>We don't have a way to track experiment. Therefore, we don't have any information about previous experiments.</li>
    <li>Training a BERT model taking up too much RAM (~7GB RAM) and Colab provides us with 12.7GB RAM. So we need to find technology that cooperates well with Colab.</li>
</ol>
<h3><i>b. Solve the problems</i></h3>
<p>Dagshub is the solution to the above problems. It's similar to Github but with many advanced functionalities including DVC and MLFlow. Specifically:
</p>
<ul>
    <li>DVC helps tracking large files such as model.pkl, data; while; the performance of "git pull" is remained effective.</li>
    <li>MLFlow helps tracking experiments run on Colab. You can view all the metadata relating to an experiment on MLFlow UI.</li>
    <li>The best thing is Dagshub is a fully integrated environment so no need for OAuth2, which means that we can access to all Dagshub functionalities on Colab (or any cloud machine) without the need of the local machine.</li>
    <li>MLFlow repo can be used to store model which is accessible everywhere, provided that you have the correct credentials. This also suggesting that it a perfect place to deploy model.</li>
</ul>
<h2>II. Parameterized Notebook</h2>
<p>
    Since all the code is performed on Colab notebook so learning how to parameterized a notebook is needed.
</p>
<h3><i>a. Problems</i></h3>
<p>Allow me to list some problems we had before:</p>
<ol>
    <li>Everytime we want to running the notebook, we have to open colab and run them cell by cell, which is anoying.</li>
    <li>It's difficult to store data produced by the notebook.</li>
</ol>
<h3><i>b. Solve the problems</i></h3>
<p>Papermill is the solution we're all argeed and it is easy to use. However, you do need jupyter notebook installed on local machine to add tag to a colab notebook.</p>
<ul>
    <li>You can run a notebook using command line. Provided that the notebook has a parameters cell.</li>
    <li>You can combine papermill with DVC to create data pipeline which defines how raw data will be processed and inferred. This is suggesting that we can write API to use our model.</li>
</ul>
<h2>III. Fine tune a BERT</h2>
<p>As we have discussed before, the BERT model is used to do sentimental analysis which is assigning label to news.</p>
<h3><i>a. Problems</i></h3>
<p>Allow me to list some problems we had before:</p>
<ol>
    <li>We don't know how good the model is at labeling news.</li>
    <li>The BERT model took too much time to train.</li>
    <li>The raw news data is skewed.</li>
    <li>Somehow training BERT model takes up to 12.7 GB RAM.</li>
</ol>
<h3><i>b. Solve the problems</i></h3>
<p>To solve abobe problems I decided to split the big notebook into 3 smaller notebooks corresponding to 3 stages: {Preprocess, Train, Evaluate}.</p>
<p>
    The Preprocess notebook takes the raw news data and transforms them into tensorflow.data.Dataset supported for large dataset. This notebook has 2 choices for splitting data which is either k-fold cross validation or normal train_test_split. 
</p>
<p>
    The Train notebook takes the data produced by the Preprocess notebook and begins training. The whole training process is tracked by MLFlow so you can view the result on MLFlow UI later.
</p>
<p>
    The Evaluate notebook import the test dataframe and transforms it to tf.data.Dataset internally. Then the preprocessed data is pushed to the imported model resulting in a classification report and ROC curve. The ROC curve can tell how good our model is at classifying label. And the lastest experiment gave a quite good ROC curve.
</p>