# Academia Sinica Diverse MWP Dataset (ASDiv) V1.0

This repository provides ***ASDiv*** (a new diverse dataset in terms of both language patterns and problem types) for evaluating and developing MWP Solvers. It contains 2305 english Math Word Problems (MWPs), and is published in this paper "[A Diverse Corpus for Evaluating and Developing English Math Word Problem Solvers](https://www.aclweb.org/anthology/2020.acl-main.92/)".



## Format
This dataset uses XML format for each MWP:
```xml
<Problem ID="nluds-0001" Grade="1" Source="http://www.k5learning.com">
	<Body>Seven red apples and two green apples are in the basket.</Body>
	<Question>How many apples are in the basket?</Question>
	<Solution-Type>Addition</Solution-Type>
	<Answer>9 (apples)</Answer>
	<Formula>7+2=9</Formula>
</Problem>
```

Each **Problem** cell includes the corresponding 3 attributes and 5 properties (*Body*, *Question*, *Solution-Type*, *Answer*, and *Formula*):

+ Problem attributes:
    + **ID**: a unique 10-bytes character identifier.
    + **Grade**:  a grade level indicating the level of difficulty. 
    + **Source**: an url identifying the reference source where the MWP came from.

+ Problem properties:
    * **Body**: the problem text includes facts and clues for solving an MWP.
    * **Question**: the text identify the question to solve.
    * **Solution-Type**: a tag which indicates a crucial math operation pattern for solving an MWP. Currently, we provide 24 different common solution types. Details are shown in our paper.
    * **Answer**: the annodated answer (includes associated measurement units if exists).
    * **Formula**: the annotated formula.


## Multiple-Step MWPs

<p align="center">
	<kbd>
		<img  width="450"  src="figs/expressiontree.png" />
	</kbd>
</p>

For multiple-step MWPs, the formula can be represented as an expression tree. The non-leaf nodes are operations and the leaf-nodes are operands. We denote the operation in the root node to be the **Solution-type** of this MWP, and the other operations on the non-leaf nodes are sub-types (in a depth-first travel manner) of the MWP and are denoted in the **Subtype** attribute of the **Solution-type**. 


```xml
<Problem ID="nluds-2262" Grade="3" Source="http://www.commoncoresheets.com">
  <Body>Sam invited 9 friends to a birthday party, but 6 couldn't come. If he wanted to buy enough cupcakes so each person could have exactly 2,</Body>
  <Question>how many should he buy?</Question>
  <Solution-Type Subtype-1="Subtraction">Multiplication</Solution-Type>
  <Answer>6 (cupcakes)</Answer>
  <Formula>(9-6)*2=6</Formula>
</Problem>
```

## Evaluation
We provide two Fold-ID sets that used in our N-folds cross-validation performance evaluation. One is for the arithmetic subset and another is used for the whole set, you can access them in the **dataset/nfolds/asdiv-a** and **dataset/nfolds/asdiv-w** sub-directories respectively.


## Citation
This dataset is released under the CC BY-NC 4.0 license, and constructed by [Natural Language Understanding laboratory](http://nlul.iis.sinica.edu.tw/), Institute of Information Science, Academia Sinica. If you find this work useful for your research, please cite our paper:

```
@inproceedings{miao-etal-2020-diverse,
  title={A Diverse Corpus for Evaluating and Developing English Math Word Problem Solvers},
  author={Miao, Shen-yun and Liang, Chao-Chun and Su, Keh-Yih},
  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
  pages={975--984},
  year={2020}
}
```


## Issues
Please contact ccliang@iis.sinica.edu.tw for any suggestions, comments, and issues. 
