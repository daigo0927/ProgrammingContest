- [AtCoder Problems](https://kenkoooo.com/atcoder/) メモ
  - [ABC120](https://atcoder.jp/contests/abc120/tasks): UnionFind
	- C: 2色のキューブが計n個積まれて与えられる．
	隣接した色が異なる部分を除去していくときの除去キューブ数の最大値．
	最終的に片方が多い分だけ残るので，それを全体から引く．
	- D: n個の島がm本の橋で繋がっている（無向グラフ）．
	橋を順番に除去したときの各場合における非連結となる島の組み合わせ．
	逆順に橋を追加していくように考える．
	UnionFindによって島同士の連結状態と連結成分のサイズを管理し，各橋を追加したときの答えを計算する．
  - [ABC119](https://atcoder.jp/contests/abc119/tasks): 全探索，しゃくとり法（？），二分探索．
	- C: n本の竹を魔法でつなぎ合わせて目標の長さの3つの竹を得るときの消費MPの最小値．
	魔法（連結・伸縮）の順番を入れ替えても結果は同じ，かつn<=8なのでそれぞれの竹の各3本への割り当て方（4**8）を全探索する．
	- D: a個の神社とb個の寺が一直線上に存在する．
	q個のパターンの座標xそれぞれにおける，神社と寺をそれぞれ1つ訪れるときの移動距離の最小値．
	ある座標xにおいて神社・寺それぞれ前後一つずつをチェックすれば良いので，これを二分探索し可能な経路（8パターン）の最小値が対象のxに対する答えとなる．
	q個のxをソートし，端からしゃくとり法によって答えを求めた後に元の順番にソートし直しても良い．
  - [ABC118](https://atcoder.jp/contests/abc118/tasks): 最小公倍数，DP．
	- C: 異なる体力を持つn体のモンスターが存在する．
	モンスターは攻撃しあい，攻撃されたモンスターはしたモンスターの体力分体力が減る．
	このときの最後に生き残るモンスターの残存体力の最小値．体力の最大公約数が答えとなる．
	- D: マッチの本数nと作れる数字aが与えられる．
	このときちょうどn本使って作れる数字の最大値．
	DP+経路復元の問題．実装上はi（<=n）本ちょうど使って作れる数字の最大値としてDPを回すのが簡単．
  - [ABC117](https://atcoder.jp/contests/abc117/tasks): bit演算．
	- C: m個の目標座標が与えられる．これに対してn個の駒を任意の座標においてから動かし，各目標座標を訪れる．
	このときの移動の総和の最小値．駒の数n-1の隣接する座標間は移動せずに済むので，座標間距離（m-1個）をソートして小さい方からm-n個の総和．
	- D: n個の非負整数aとさらにkが与えられる．k以下の数を用いたときの，各aに対するxorの総和の最大値．
	xorの総和なので各aの各桁でいくつbitが立っているかを計算し，多いbitに対応するようにbitを決める（1が多いなら0）．
	k以下という制限付きなのでkの上位bitから見ていき，kを超えないように処理していく．
  - [ABC116](https://atcoder.jp/contests/abc116/tasks): 強いて言えばソート
	- C: 複数の花に水をやる（連続した花の高さを+1）ことで目標の高さに育てる．このときの水やり回数の最小値．
	目標の高さから引いていけば良い．途切れるor端まで行って再開したら回数+1
	- D: ネタとおいしさを持つn個の寿司が与えられる．k個食べるときの満足度=美味しさの総和+ネタの種類^2で定義するときの最大値．
	美味しさでソートした上位k個を初期値とする．
	さらに満足度を増やすにはネタ数を増やすしかないので，ネタ数を増やしながらダブってるネタをおいしさの小さいものから捨てていけば良い．
  - [ABC115](https://atcoder.jp/contests/abc115/tasks): ソート，再帰．
	- C: 高さのあるn本の木から最小値と最大値の差が最小となるようにk本の木を選ぶ．このときの差の最小値．
	ソートして端から最小値を探せば良い．
	- D: パンとパティからなるフラクタル的なハンバーガーを下からx層食べる．このとき食べるパティの枚数．
	下から半分以下・以上の場合に分けて再帰し，パティの枚数を加算していく．
  - [ABC114](https://atcoder.jp/contests/abc114/tasks): 全探索．素因数分解
	- C: n以下の整数のうち753数（7,5,3をそれぞれ一回以上使う数字）の数を求める．準7,5,3数を列挙して全探索．
	- D: n!の約数のうち75数（約数が75個の数）の個数を求める．n!を素因数分解する．素因数の乗数で75数を作れる組み合わせを総和する．
  - [ABC113](https://atcoder.jp/contests/abc113/tasks): 辞書型ソート，DP
	- C: 県と所属する市が与えられ，県ごとに市に番号をふる．辞書型ソート．
	- D: あみだくじの縦棒が与えられる．右上から指定のゴールに行くための横棒置き方．DP．
  - [ABC112](https://atcoder.jp/contests/abc112/tasks): グリッドサーチ，最大公約数
	- C: ピラミッドがある場所の各地点の高さが与えられる．ピラミッドの高さを求める．対象空間が狭いので地点をグリッドサーチ．
	- D: 総和が与えられる複数の数について，それらの数の最大公約数の最大値を求める．約数を全列挙してそれぞれ条件を満たす最大値．
  - [ABC111](https://atcoder.jp/contests/abc111/tasks): 場合分け，累乗の足し算
	- C: 与えられた数列について，\/\/となるように書き換える回数の最小値．偶数位置と奇数位置で最多数の数字を数え，場合分け．
	- D*: 複数の腕からなるロボットアームに対して，複数の座標が与えられる．アームの先端が各座標に到達するための各アーム部位の長さと操作方法を求める．
	1,2,4,とアームをつけていくと近い場所も遠い場所も対応できる．部分点は長さ1のアームをたくさん用意すれば可能．
  - [ABC110](https://atcoder.jp/contests/abc110/tasks): 文字列操作，場合の数，素因数分解．
	- C: ２つの文字列s,tが与えられる．s内の二種類の文字を交換する操作によってtにできるかどうか．
	ユニークな各文字の個数は変わらないので，各文字の個数をs,tでカウントして一致すれば実現可能．
	- D: 正整数mが与えられる．n個の整数aの積によってmを表すときの場合の数．
	mを素因数分解する．各素因数の乗数をn個に割り振る問題（乗数分の球とn-1個の仕切りの並べ方）と考えられる．これを全素因数でかけたものが答え．
  - [ABC109](https://atcoder.jp/contests/abc109/tasks): 最大公約数，貪欲法
    - C: １次元上の複数の座標が与えられ，全てを訪れることのできる歩幅の最大値．全座標の最大公約数を求める．
    - D: 二次元のグリッドに積まれたコインについて，偶数枚のマスを最大にするときのコインの操作方法．左上から下（または右）へGreedyに押し付けていけばいい．
  - [ABC108](https://atcoder.jp/contests/abc108/tasks): 場合分け，全探索，グラフ，2の累乗
    - C: a+b, b+c, c+aが全てkの倍数になるような（a, b, c）の組み合わせ．偶奇で場合分け．全探索でもいける．
    - D: 始点から終点までにL本のコスト0〜L-1のパスを持つ有向グラフの作成．
	はじめに2の階乗でパスを張り，足りない点を補うように経路を足していく．
  - [ABC107](https://atcoder.jp/contests/abc107/tasks): 
	- C: 数直線上に置かれたn本のろうそくの内k本に火をつける．
	原点から開始するときの移動距離の最小値．k本つけるときの移動距離を端から計算すれば良い．
	- D**: 数列aに対して全通りの部分区間の中央値からなる数列bを考える．この中央値列bの中央値を求める．
	長さmの数列内の中央値xは，x以上の要素をceil(m/2)個以上含む数の最大値と言える．これを二分探索することになる．
	aの部分列に対する，x以上の要素の個数を基準に探索していく．
	aの各部分列に対するx以上の要素数の判定には，aの要素をxとの大小に応じて±1に書き換えた上で，累積和を計算する．
	最終的に累積和の数列に対して転倒数を求める問題として考えることができる．
  - [ABC106](https://atcoder.jp/contests/abc106/tasks): 累積和
    - C: 数字の長さが増えていく問題．２以上は実質無限長になるので1をいくつ含むかで判定．
    - D: 指定された区間内を何本の列車が通る（完結）するか．
	列車の始点と終点を２次元座標と考えて，二次元累積和によってO(1)で条件を満たす列車の本数が計算できる．
  - [ABC105](https://atcoder.jp/contests/abc105/tasks): 2進数の考察，累積和，ハッシュマップ
    - C: −2進数の問題，２進数と同様に小さい桁から処理すればいける．
    - D: 連続した値を足して与えられた値で割り切れるかどうか．累積和をとって余りをハッシュで管理．
  - [ABC104](https://atcoder.jp/contests/abc104/tasks): bit全探索，DP，累積和
    - C: 目標点数に到達するための最小解答数．中途半端に解くのはたかだか一つ．bit全探索．
    - D: 文字列を置換して何通りの'ABC'を作れるか．DPか累積和と組み合わせ．
  - [ABC103](https://atcoder.jp/contests/abc103/tasks): mod，グラフ．
	- C: n個の整数aが与えられる．各aとのmodの総和の最大値を計算する．全てのaの最小公倍数−1によって計算した値が答え．
	- D: n個の島が一列に繋がっている．指定された島同士を非連結にするために除去すべき橋の本数の最小値．
	非連結にする島ペアを東側の島の位置でソートする．前回落とした橋によって対象の島ペアが非連結になっているかを確認する．
	なっていなければ新たに橋を落とし，落とした橋の座標を更新していけば良い．
  - [ABC102](https://atcoder.jp/contests/abc102/tasks): 中央値，探索
	- C: 長さnの数列が与えられる．ある整数bに対してすぬけ君の悲しさabs(a_i-(b+i))を定義する．このときの悲しさの最小値．
	数列の各値からiを引いて補正する．絶対値の最小化は中央値なので補正後の数列の中央値が答え．
	- D**: 長さnの整数列aが与えられる．これを３箇所で切り，空でない4つの部分列b,c,d,eをつくる．
	それぞれの部分列の総和p,q,r,sに関して，最大値と最小値の差の最小値を求める．
	まずc,dの間（中央）の切れ目を左端に決め，そのときのpとq，rとsが近くなるように左と右の切れ目を決める．
	中央の切れ目を右に移動していくと，各場合で最適な左右の切れ目も右に移動して探せば良い．
	各場合で最大値と最小値の差を計算しておき，その中の最小値が答え．
  - [ABC101](https://atcoder.jp/contests/abc101/tasks): 
	- C: 1..nを並び替えた数列がある．連続したk個の要素をその中の最小値で置き換える操作ができる．
	このとき数列を全て同じ数字にするときの走査回数の最小値．
	1の位置を基準に左右に操作をしていけば良い．長さkの窓の中で，基準の1が来る場所を全探索．
	- D**: 整数の十進法時の桁和をsとする．正の整数nに対して，任意のm>nが(n/s_n)<=(m/s_m)を満たすときnをすぬけ数とする．
	このときすぬけ数を小さい方からk個列挙する．
	ある数nに対して，x(>n)のうち(x/s_x)を最小にするものを考えると，上位から途中のd桁まで同じ数字，d桁でnより大きく（厳密には9と言える），
	以降の下位桁は9となる数字のどれかとなる．nの桁数以下のdについて計算すれば良い．
	n=1から始めて順次これを計算，列挙すれば良い．[youtubeの解説](https://www.youtube.com/watch?v=aTMRqHCZHaA)が（比較的）わかりやすい．
  - [ABC100](https://atcoder.jp/contests/abc100/tasks): 絶対値を全探索
  	- C: 与えられた数列中の任意の数を２で割っていく．何回２で割れるか．全部割っていく．
	- D*: 綺麗さ・美味しさ・人気の3つの数値（負もある）を持つ複数のケーキが与えられる．
	それぞれの指標の和の絶対値の和の最大値を求める．各指標の和が正負の場合：計8通りを探索し，最大値を返せば良い．
  - [ABC099](https://atcoder.jp/contests/abc099/tasks): DP，TLEへの注意
  	- C: 1と6の累乗，9の累乗のみを何回足せば目標の値になるか．上限が小さいのでDP．bit全探索でもできるかも．
	- D: 二次元のマスを3で割ったあまりが同じものが同じ色になるように塗る．塗る前と後の色によってコストが発生する．
	コストの総和の最小値を求める．普通にやるとTLEなので処理をまとめる．
  - [ABC098](https://atcoder.jp/contests/abc098/tasks): TLEへの注意．尺取り法．
  	- C: 左右を向いている人たちが一列に並んでいる．ある位置に向きを変える人数の最小値．
	二乗オーダーだとTLEなので値を保持して線形オーダーで処理する．
	- D*: 与えられる数列について，総xorと総和が等しい区間の数を求める．
	bitが重なるとxorと和がずれるので，それをチェックしながら尺取り法で線形オーダー．
  - [ABC097](https://atcoder.jp/contests/abc097/tasks): 文字列の探索．UnionFind．
  	- C: 与えられた文字列内の異なる部分文字列について，辞書順で指定された順番のものを求める．
	指定はたかだか5番目なのでaで始まる部分文字列を探索，bで，，，とやって指定したものが出たらそれを返せば良い．
	- D: 1からNを並び替えた数列と位置のスワップ方法が与えられる．
	与えられた方法のみでスワップして，位置と数が同じにできるものの個数を求める．
	DFSやUnionFindによって各位置を結びつけ，移動できる数の個数を求めれば良い．
  - [ABC096](https://atcoder.jp/contests/abc096/tasks): 全探索，素数，数理的考察．
  	- C: 指定された通りにグリッドを塗れるかどうか，ただし孤立したグリッドは塗れない．
	孤立していないかを全グリッドで判定すれば良い．
	- D: N個の異なる素数，かつその内任意の5個の和が合成数となる数列を求める．
	下一桁が1の素数をN個求めれば条件を満たすことができる．
  - [ABC095](https://atcoder.jp/contests/abc095/tasks): 場合分け，累積和，考察．
  	- C: 値段の異なるA・B・AB半分ずつのピザを買い，指定された数のAピザ，Bピザを用意するための料金の最小値．
	ABピザを半端に買う必要はないのでそれぞれ場合分けして最小値を返す．
	- D*: 寿司間のコストと各寿司のエネルギーが与えられた回転寿司屋さんで得られるエネルギーの最大値を求める．
	どのような弧を描くかで探索する．累積和も使う．
  - [ABC094](https://atcoder.jp/contests/abc094/tasks): 中央値，combination
  	- C: 偶数長の数列が与えられる．各数字を抜いたときの中央値を求める．
	一つの数字しか抜かないので中央値はたかだか2パターン．抜く数字の大小で判定できる．
	- D: n個の数字が与えられる．ここから二つの数字を選んだときのcombinationの最大値．
	片方はできるだけ大きい数字，もう片方はその半分に近いほどcombinationが大きくなるためそれを探す．
  - [ABC093](https://atcoder.jp/contests/abc093/tasks): 場合分け
  	- C: 3つの整数が与えられる．2つを+1する，1つを+2するという処理を用いて全てを等しくするための処理数の最小値．偶奇で場合分け．
	- D**: 2回のコンテストから算出されるスコアを考える．高橋くんがそれぞれA，B位（スコアはA*B）のときの，高橋くんよりスコアの小さい人の最大値．場合分け．
  - [ABC092](https://atcoder.jp/contests/abc092/tasks): 場合分け，
  	- C: 一次元上に座標を持つ複数の観光スポットがあり，移動距離に応じてお金がかかる．
	各スポットをスキップしたときの費用の総和を求める．
	各スポットをスキップした場合の前後のスポット間の費用を計算しておく．
	- D: ある大きさのグリッドを白黒に塗り分ける．白と黒の連結成分を指定された数にするときの塗り分け方法を求める．
	グリッドの全域が大きいので真っ白の中に黒（逆も同じ）を必要な個数作れば良い．
  - [ABC091](https://atcoder.jp/contests/abc091/tasks): bit演算．
  	- C*: N個ずつの赤と青の二次元座標が与えられる．
	赤のx,y座標が青のx,y座標よりも小さいときその二つをペアにできる．このときのペアの最大値を求める．
	任意の青い点に対して，y座標がギリギリの赤い点をペアにしていけば良い．
	- D**: 二つの長さNの数列a,bからN^2通りの組み合わせの和を考える．これらの総xorを求める．
	bitごとに偶数個あるか奇数個あるかを考える．pythonだと工夫しないとTLEになる．
  - [ABC090](https://atcoder.jp/contests/abc090/tasks): 
	- C: 
    - D: 
  - [ABC089](https://atcoder.jp/contests/abc089/tasks): 
	- C: 
    - D: 
  - [ABC088](https://atcoder.jp/contests/abc088/tasks): 
	- C: 
    - D: 
  - [ABC087](https://atcoder.jp/contests/abc087/tasks): 
	- C: 
    - D: 
  - [ABC086](https://atcoder.jp/contests/abc086/tasks): 
	- C: 
    - D: 
  - [ABC085](https://atcoder.jp/contests/abc085/tasks): 
  	- C: 
	- D: 
  - [ABC084](https://atcoder.jp/contests/abc084/tasks): 
  	- C: 
	- D: 
  - [ABC083](https://atcoder.jp/contests/abc083/tasks): 
  	- C: 
	- D: 
  - [ABC082](https://atcoder.jp/contests/abc082/tasks): 
  	- C: 
	- D: 
  - [ABC081](https://atcoder.jp/contests/abc081/tasks): 
  	- C: 
	- D: 
  - [ABC080](https://atcoder.jp/contests/abc080/tasks): 
  	- C: 
	- D: 
  - [ABC079](https://atcoder.jp/contests/abc079/tasks): 
	- C: 
	- D: 
  - [ABC078](https://atcoder.jp/contests/abc078/tasks): 数理的考察
	- C: n個のテストケースに対してmケースで危うい解法，n-mケースで確実な解法を提出するときの全ACまでの時間の期待値．
	総ACまでの時間に関して方程式を立てられるのでそれを解く．
	- D*: 2人のプレイヤーが山札とカードを交換していく．最終的な2人の手札の差の絶対値の最大値を求める．
	最終的に二枚のカードしか比較しないので初手で一枚残すか全部とるかのみを考えれば良い．
  - [ABC077](https://atcoder.jp/contests/abc077/tasks): 
    - C: 三種類の祭壇のパーツA，B，Cが様々な大きさでそれぞれN個与えられる．
    ABCの順番で上から積んでいき祭壇を作る．下のパーツほど大きくなければならないとき，作れる祭壇の種類数を返す．
    ABCそれぞれについて降順にソートする．A（B）の各パーツについて，それより小さいB(C)のパーツの個数をカウントする．
    Bの各パーツに対するそれより小さいCのパーツ数の累積和をとる．
    Aの各パーツに対するそれより小さいBのパーツ数を上記の累積和から参照し，答えに足していく．
    - C: （別解）A,Cをソートしておき，Bの各パーツに対して使えるA，Cのパーツ数を二分探索によって計算する．
    - D: 整数kが与えられる．正の倍数の１０進法での各桁の和の最小値を返す．
    任意の整数について，１足すと桁和も１増える．また１０倍しても桁和は不変である．
    1の加算をコスト1の経路，１０倍をコスト0の経路として，0~k-1の値を頂点からなるグラフを考える．
    頂点1からスタートして頂点0（kの倍数）への最小コストを計算し，+1したものが答えとなる．
    01BFS（両端queue）を用いる．
  - [ABC076](https://atcoder.jp/contests/abc076/tasks): 
    - C: オリジナルの文字列Sを想定する，そのうちいくつかが？に置換された文字列S'，およびSの部分文字列Tが与えられる．
    このときS'およびTから復元できるオリジナルの文字列Sのうち，辞書順で最初のものを返す．
    S'を左から見ていき，各位置についてTをマッチングしていく．マッチングが可能なら答えの候補にしていき，
    最後に辞書順最初のものを返す．
    - D: ある列車について，時間tの数列と制限速度vの数列が与えられる．
    始点と終点は停止しており，加減速を１m/sとするとき，制限速度に従ったときの移動距離の最大値を返す．
    0.5秒ごとに速度を管理しておき，最後に積分する．速度の変化する点に注意する．
  - [ABC075](https://atcoder.jp/contests/abc075/tasks): 
    - C: 無向（連結）グラフが与えられる．グラフを構成する辺のうち，除外するとグラフが分断される（非連結になる）辺の本数を返す．
    各辺を除外し場合について，任意の頂点から到達できない点が存在しないかを全ての辺について試す．
    - D: 二次元平面上のN個の点が与えられる．各辺がxy軸に平行で，内部（辺上含む）にk個以上の点を含む長方形の面積の最小値を返す．
    まずx軸（y軸でも可）に平行な辺を決める．その上でy軸に平行な辺の片方を決める．
    最後のy軸に平行な辺はk個以上の点を内包しなければいけないので決定できる．
    これを全通り試し，面積の最小値を返す．
  - [ABC074](https://atcoder.jp/contests/abc074/tasks): 
    - C: ビーカーに二通りの分量の水と，二通りの分量の砂糖を入れられる．また水100グラムに溶ける砂糖の量が与えられる．
    ある値以下の質量で，できるだけ濃度の高い砂糖水を作るときの，砂糖水および砂糖の質量を返す．
    水の質量全通りに対して，全通りの砂糖の質量を試せば良い．
    - D: 都市間の距離が無向グラフで表現される国について，全点間の最短距離を表す（？）距離行列が与えられる．
    与えられた全点間の最小距離が正しいか判定する．正しい場合はそこで存在する経路長の和の最小値を返す．
    まずダイクストラ法などで全点間の最短距離を再計算する．与えられたものと違ければ経路構造は存在しない．
    合っている場合は各点のペアについて，直接移動する経路を除外したときの最短距離を計算する．
    直接以外の経路で真の最短経路長と一致するなら，直接結ぶ経路は冗長であるので除外する．
    経路を取捨選択した後，最後に全経路長の和を返せば良い．
  - [ABC073](https://atcoder.jp/contests/abc073/tasks): 
    - C: 数字が順番に与えられ，これを管理する．与えられた数字が手元になければ追加，あれば削除を行う．最後に手元に残った数字の個数を返す．
    奇数回出てきた数字の数を返せば良い．
    - D: 都市間の距離が無向グラフで表現される国が与えられる．この都市を任意の順番で移動するときの移動距離の最小値を返す．
    まずワーシャルフロイド法などで全点間の最短距離を計算する．訪れる都市数が少ないので全ての順列を試し，経路の最小値を返せば良い．
  - [ABC072](https://atcoder.jp/contests/abc072/tasks): 
    - C: 数列が与えられる．数列中の各値に対して±1を行うか，何もしないかができる．
    このとき各値に処理を行った後の重複する数の最大値を返す．各数字とその±1の値の出現回数を管理しておき，最大値を返せば良い．
    - D: 1からNの数字からなる順列が与えられる．この順列の隣り合う数をスワップする操作を行える．
    このとき．左から数えた位置とその位置の数字が異なるようにするために行う操作回数の最小値を返す．
    左から操作が必要か判定していき，操作が必要なら右の数字とスワップする（最後だけ逆），ということを順にやっていけば良い．
  - [ABC071](https://atcoder.jp/contests/abc071/tasks): 
    - C: 一様でない長さのN本の棒が与えられる，作ることのできる最大の長方形の面積を返す．
    数字がダブってるもののうち大きい方から二つ取れば良い．4つあれば４辺全部同じ数字．
    - D: 2xNのタイルに，1x2の大きさの３色のドミノを同じ色のドミノが隣接しないように敷き詰めていく．このときの敷き詰め方を返す．
    部分的に見ると，ドミノを縦にして一つ置くか，横にして二つ置くかなのでこれを繋げていって場合の数を増やしていけば良い．
  - [ABC070](https://atcoder.jp/contests/abc070/tasks): 
    - C: N台の時計があり，それぞれの周期で針が周るとき，全ての針が同時に真上を向くまでの時間．各周期の最小公倍数を求めれば良い．
    - D: 頂点数N，頂点のペアがある距離で結ばれた木が与えられる．はじめに頂点kが指定される．
    このとき頂点xから頂点yまで頂点kを介して移動するときの最短距離を返す．最初に頂点kから全頂点への最短距離をDFSなどで計算しておき，
    渡されたx,yについk-xとk-yの距離を足せば良い．
  - [ABC069](https://atcoder.jp/contests/abc069/tasks): 
    - C: 与えられた数字の集合を並び替えたとき，任意の隣接する数字の積が４の倍数にできるかどうかを判定．奇数は４で挟まなければならない．
    また４の倍数でない偶数は全て隣接させて数列の端に置かなければならない．この二つを行うのに４の倍数が十分含まれているかを判定する．
    - D: HxWのタイルをN色で，同じ色が分裂しないような塗り分け方を返す．端から順番に一筆書きで塗っていけば良い．
  - [ABC068](https://atcoder.jp/contests/abc068/tasks): 
    - C: 与えられたグラフ上の二点が二近傍で結ばれているかどうか．両方を結合相手に含む頂点があるかを計算すれば良い．
    - D: 長さNの数列のうち最大のものをN減らし，他の要素を１ずつ増やす．この操作を最大値がN-1になるまで行う．
    操作の回数がちょうどk回になるときの元の数列を返す．最終形を決めてから処理を逆算すれば良い．
  - [ABC067](https://atcoder.jp/contests/abc067/tasks): 
    - C: 数列の前半の和と後半の和の差の最小値を求める．順番に計算するだけ．
    - D: 木構造の陣取りゲームでどちらが勝つか．最善手は相手に繋がる経路を潰していくこと．
	両方のプレイヤーについてキューを管理して各マスまでの距離を計算する．
	距離が近い方がそのマスを獲得でき，獲得マスの多い方が勝利．
  - [ABC066](https://atcoder.jp/contests/abc066/tasks): 
    - C: 与えられた数列を文字列として追加・前後反転を繰り返していったものを出力．
	貪欲法だと文字列が長くなった時に処理時間が増えるので最終的な文字列における位置を逆算して挿入する．
    - D: 一種類だけ数字がダブってる数列について，長さkの数列の作り方．ダブってる数字の間の数を使わなかった場合が重複するので，それを計算して引く．
  - [ABC065](https://atcoder.jp/contests/abc065/tasks): 
    - C: 犬と猿を隣り合うように一列に配置する方法．それぞれの頭数に応じて場合分けして組み合わせ（階乗）．
    - D: 最小コストで街をつなぐ方法．全域探索木（MST）．プライオリティキューかUnionFold木．
  - [ABC064](https://atcoder.jp/contests/abc064/tasks): 
    - C: AtCoderコンテスタントの色の種類．最高レート帯の人の配色が重要．
    - D: '('と')'でできた文字列を完成させる．それぞれの数を管理．
  - [ABC063](https://atcoder.jp/contests/abc063/tasks): 
    - C: 10で割り切れない最大の得点数を求める．簡単．オーバーだけどDPでも解ける．
    - D: 魔物の群れを倒すための最小の呪文回数．ある回数で足りるかどうかを二分探索．基準ダメージ（b）と追加ダメージ（b-a）に分けて考える．
  - [ABC062](https://atcoder.jp/contests/abc062/tasks): 
    - C: 横縦幅が与えられた長方形をなるべく同じ大きさに三分割するときの面積差の最小値．4種類の分割方法で場合分け．
    - D: 3N個の数字から前の方N個の和と後ろの方N個の和の差の最小値．前半は最小値を捨てていきたいので，使う数字をヒープで管理しながら和を計算していく．
    逆に後ろの方は最大値を捨てていきたいので，マイナスの値をヒープで管理しながら和を計算していく．最後に差を計算する．
  - [ABC061](https://atcoder.jp/contests/abc061/tasks): 
    - C: 重複ありの数列のうち，k番目に小さい数を出力する．数字ごとにカウントしてkを超えたら出力．
    - D: 重み付き有向グラフの辺の重みをスコアとして，ある地点からある地点へのスコアの最大値を出力する．重みを反転させて最短経路問題として解ける．
    重みは正負両方の値をとるのでダイクストラ法は使えず，ベルマンフォード法を使う．これなら閉経路も検出できる．
    経路探索は負閉路がないとき最大N-1回なので，これより多い時は負閉路がある．
  - [ABC060](https://atcoder.jp/contests/abc060/tasks): 
    - B: 任意のAの倍数をBで割った余りがCとなることがあるかどうか．Bで割った余りがループする前に条件を満たすかどうか判定．
    - C: 一定時間水が出る蛇口を数人が各時刻でひねった時，計何分水が出ているか．場合わけで足し算．
    - D: ナップザック（一定の重さを超えずに物をいくつ持てるか）問題．普通はDPだが重さの種類が少ないという条件付きなので，各重さの個数をカウントして全探索できる．
  - [ABC059](https://atcoder.jp/contests/abc059/tasks): 
    - C: 
    - D: 
  - [ABC058](https://atcoder.jp/contests/abc058/tasks): 
	- C: 
    - D: 
  - [ABC057](https://atcoder.jp/contests/abc057/tasks): 
	- C: 
    - D: 
  - [ABC056](https://atcoder.jp/contests/abc056/tasks): 
	- C: 
    - D: 
  - [ABC055](https://atcoder.jp/contests/abc055/tasks): 
	- C: 
    - D: 
  - [ABC054](https://atcoder.jp/contests/abc054/tasks): 
	- C: 
    - D: 
  - [ABC053](https://atcoder.jp/contests/abc053/tasks): 
	- C: 
    - D: 
  - [ABC052](https://atcoder.jp/contests/abc052/tasks): 
	- C: 
    - D: 
  - [ABC051](https://atcoder.jp/contests/abc051/tasks): 
	- C: 
    - D: 
  - [ABC050](https://atcoder.jp/contests/abc050/tasks): 
	- C: 
    - D: 
  - [ABC049](https://atcoder.jp/contests/abc049/tasks): 
	- C: 
    - D: 
  - [ABC048](https://atcoder.jp/contests/abc048/tasks): 
	- C: 
    - D: 
  - [ABC047](https://atcoder.jp/contests/abc047/tasks): 
	- C: 
    - D: 
  - [ABC046](https://atcoder.jp/contests/abc046/tasks): 
	- C: 
    - D: 
  - [ABC045](https://atcoder.jp/contests/abc045/tasks): 
	- C: 
    - D: 
  - [ABC044](https://atcoder.jp/contests/abc044/tasks): 
	- C: 
    - D: 
  - [ABC043](https://atcoder.jp/contests/abc043/tasks): 
	- C: 
    - D: 
  - [ABC042](https://atcoder.jp/contests/abc042/tasks): 
	- C: 
    - D: 