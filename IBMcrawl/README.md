# My First Attempt in the Field of Text Analysis or NLP




The project is aimed at finding annual 'Hot Word' in all IBM official articles, posted in its press release website, on the topic of Cloud Computing, from the year 2008 through 2015, by which to get a glimpse of IBM vision towards Cloud Computing.

The dataset, crawled with the help of Scrapy, contains 774 articles and 595630 English words.

###Text Analysis techniques applied:

* Text Representation

  * Tokenization
  * Stemming
  * Bag-of-Words
  * Part-of-Speech
  * TFIDF

###Tools for analysis:

* Python NLTK package
* Tableau for word cloud Visualization.

###Analysis Methodology Summary:

*	Use a simple bag-of-words approach 
*	Use a bag-of-words with stemming and stop word removal approach
*	Use a bag-of-words with stop word and customized word removal approach 
*	Use POS and focus on NNP approach
*	Customized Python scripts to filter out common frequency words among years and find out unique frequency words for a particular year.

(Please refer to the Report in the folder 'Document' for detailed information.)


###Conclusion of this Mini-project:

1. Using bag-of-words with stopwords and customized words removal, but without stemming, can greatly imporve the performance of output:the intuition of 'Hot Words' differs from year to year and is quite revealing.

2. It’s reasonable to make a guess that IBM cloud computing business has shifted its target from government institution (as words “president” “state” “students” “Carolina” appeared a lot in early years) to commercial market(“marketing”, “trademarks”) in the middle of time period concerned and, in the end, towards technological innovation field(“innovation”, “digital”,”softlayer”).

3. The word of “big” stands out in the year 2013, which may indicates the popularity of “Big Data”. 

4. Bluemix, which is a hot IBM business nowadays, was first mentioned in the year 2015 with another word “health”, both of are known as IBM core business.
