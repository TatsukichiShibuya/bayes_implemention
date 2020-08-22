# bayes_implemention
"ベイズ推論による機械学習", "ベイズ深層学習", "変分ベイズ学習"の実装

## プログラム解説
### ベイズ深層学習
1. 2-chapter4/compare_sampling.py
棄却サンプリングとメトロポリスハスティングス法とハミルトニアンモンテカルロ法を比較  
* 目標  
確率密度pからサンプリングしたい。  
* 設定
任意のzについて、pに比例するp_childaにおける確率p_childa(z)は計算できる。p_childaからはサンプリングできない。(p=N(3,2)、p_childaはpの係数を除いたもの))
棄却サンプリング
