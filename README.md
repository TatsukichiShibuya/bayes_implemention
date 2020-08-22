# bayes_implemention
"ベイズ推論による機械学習", "ベイズ深層学習", "変分ベイズ学習"の実装

## プログラム解説
### 2-chapter4/compare_sampling.py
棄却サンプリングとメトロポリスヘイスティングス法とハミルトニアンモンテカルロ法を比較  
* 目標  
確率密度pからサンプリングしたい。  
* 設定  
任意のzについて、pに比例するp_childaにおける確率p_childa(z)は計算できる。p_childaからはサンプリングできない。(p=N(3,2)、p_childaはpの係数を除いたもの))
* 棄却サンプリング  
提案分布q(z)=Uni(-10,10)、K=20(pは実数上で定義されるが、実用上\[-10,10\]として問題ない)
* メトロポリスヘイスティングス法  
提案分布q(z|z')=N(z', 1)
* ハミルトニアンモンテカルロ法  
補助変数pは
