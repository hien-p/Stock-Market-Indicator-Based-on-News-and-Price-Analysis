<h1>Some thought on Hien works in 13th - 19th Feb 2023</h1>
<h2><i>On the first paper</i></h2>
<p><b>Objective:</b> The authors used historical stock price movements (prec) until the current week to predict the close_prec for each day in the next week</p>
<p><b>close_prec</b> is the target output of the paper.<br>It's a numeric value indicating the change precision between 2 consecutive days.<br>If it's positive -> the predicted movement is increasing and vice versa.</p>
<div>
    <p><b>Experiment:</b>There were 2 cases for regression & classification approaches proposed by the authors.</p>
    <ol>
        <li>Use training data to predict weekly basis.</li>
        <li>Use test data to predict 52 weeks.</li>
    </ol>
    <p>The training processes for each case taking the regression approach</p>
    <p><i>Case 1:</i> A CNN reads the univariate input seq of [5,7,14] days -> close_prec in the next 5 days.</p>
    <p><i>Case 2:</i> A CNN reads the multivariate input (4 feats) seq of 2 weeks (10 days) -> close_prec in the next weeks.</p>
</div>
<b>Questions:</b>
<ol>
    <li>What the purpose of classification metioned in the paper?</li>
    <li>Why they used precision instead of prices?</li>
    <li>What happened to case 2?</li>
    <li>Why the output Dense(1)?</li>
    <li>Do they combined all historical prices or segmented they by days?</li>
    <li>Can the date be used as an input?</li>
</ol>

<hr>

<h2><i>On the second paper</i></h2>
<p>
    <b>Objective: </b><q>In [2] paper, a deep learning model based on Convolutional Neural Network is proposed to predict the stock price movement of Chinese stock market</q> from <a href="https://harryph.notion.site/My-Note-1d5c348aea7740f8887fea77944696a0">Hien_Notion</a>
</p>

<p>
    <b>Approach:</b> They did a classification problem with 2 labels which are up or down.
    <ul>
        <li>Input: X = (x1, x2,..., xm) -> a m x 5 matrix</li>
        <li>Output: Y = (y1, y2,..., ym) -> a m x 1 matrix</li>
        <li>Normalize data: They used min max normalization</li>
        <li>Dataset: They wrote a function to generate labels. It take a price of day A compared with 10 days after A. If mostly is up then label for A is 1</li>
    </ul>
</p>

<div>
    <b>Questions:</b>
    <ol>
        <li>Why vectorized input data?</li>
    </ol>
</div>