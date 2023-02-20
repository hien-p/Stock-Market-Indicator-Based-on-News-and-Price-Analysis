<h1>Experiment</h1>

<h3 style='color:green;'>Name: Predicted Price Adjustment</h3>

<p>Prepare</p>
<ul>
	<li>BERT</li>
	<li>LSTM</li>
	<li>history prices</li>
	<li>article news/title</li>
</ul>

<p><i>Idea:</i> We can train a neural net to predict prices, however, they are sometime not close to the original. So the idea is to add the news factor to adjust them so that they are closer to their original prices.</p>

<p><i>Target:</i> To predict better at longer ranges. e.g. a week, two weeks,...</p>

<p><i>Reason:</i> LSTM model submitted in ML final didn't preform well on week prediction</p>

<p style='color:green;'>Steps:</p>
<div>
	<p>Train a LSTM model with history prices of one company -> a price prediction model.</p>
	<p>Predict the prices of that company within the next week -> an array of future prices within a week.</p>
	<p>Assume that the real predicted price = [75% future price, 25% news]</p>
	<p>The 75% future price is the predictions from the LSTM model</p>
	<p>The 25% news is calculated as below:</p>
	<ul>
		<li>We collect the news from one moth before the prediction week and label them -> array of labels.</li>
		<li>Aggregate the label array -> label weight</li>
		<li>Calculate the adjusted prediction with the formula.<br>	
		<i>CT: adjusted prediction = predicted price + label weight*(predicted price/75)</i></li>
	</ul>
</div>