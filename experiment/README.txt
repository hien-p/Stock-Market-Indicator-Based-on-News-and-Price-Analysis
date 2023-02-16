---> Experiment

Name: Predicted Price Adjustment

Prepare: {BERT, LSTM, history stock prices, article news}

Idea: We can train a neural net to predict prices, however, they are sometime not close to the original. So the idea is to add the news factor to adjust them so that they are closer to their original prices. 

Target: To predict better at longer ranges. e.g. a week, two weeks,...

Reason: LSTM model submitted in ML final didn't preform well on week prediction

Steps: 
	Note: the array of adjusted prediction is the output
	1. Train a LSTM model with history prices of one company resulting in a price prediction model.
	
	2. Predict the prices of that company within the next week -> an array of future prices within a week.
		* [Assume] Each predicted price contributes to 75% to its adjusted prediction.
		
	3. We collect the news from one moth before the prediction week and label them -> array of labels.  
	
	4. Aggregate the label array -> label weight
	
	5. [Assume] the weight contributes the last 25% to the adjusted prediction
	
	5.	and calculate the adjusted prediction with the formula.
		
		CT: adjusted prediction = predicted price + label weight*(predicted price/75)
