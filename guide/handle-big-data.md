<h1>To handle big data</h1>
<h2>I. Problem</h2>
<p>If you're facing these problems:</p>
<ul>
    <li>Training requires too much RAM that it crash.</li>
</ul>
<h2>II. Solution</h2>
<p>You can resolve using these guides</p>
<ul>
    <li>Split the notebook into: data, train, validate notebook</li>
    <li>Preprocess the data inside the <b>data</b> notebook</li>
    <li>Save the preprocessed data as tf.data.Dataset. This method prevents pushing the whole dataset into RAMs.</li>
</ul>

