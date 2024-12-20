version = "7.0.3"

diceLogo = """

██████  ██  ██████ ███████       ██   ██ ██    ██ ███    ██
██   ██ ██ ██      ██            ██  ██  ██    ██ ████   ██
██   ██ ██ ██      █████   █████ █████   ██    ██ ██ ██  ██
██   ██ ██ ██      ██            ██  ██  ██    ██ ██  ██ ██
██████  ██  ██████ ███████       ██   ██  ██████  ██   ████
"""

activities = [
    "サイコロって呼んだら負けかなと思ってる",
    "ん、もっかい振るべき",
    "ファンブルにぶち込まれる楽しみにしておいてください！",
    "今日はダイスについて解説していくぜ",
    "いいですか、落ち着いて振ってください",
    "ここでクリティカル、インド人を右に！",
    "どけ！俺はダイス君だぞ！",
    "出目っていつもそうですね…！",
    "お前らが振らねぇ限り…俺も振らねぇからよ…！",
    "100日後に出るファンブル",
    "見て！ダイスが回っているよ かわいいね",
    "これは隠しメッセージです。次は良い出目が出るかもね",
    "平々凡々ダイス！！",
    "クリティカルのお兄さんが病気になった…",
    "あたしは1、あんたは100",
    "振りたい？……ダメ。",
    "だが出目は見事だった…いいセンスだ",
    "邪魔が入った！…また振ろう！",
    "ダイスを振るときはね、なんというか、救われてなきゃぁダメなんだ",
    "テーマパークに来たみたいだぜ 運気があがるなぁ",
]

CoC_CharacterSheet = """```\
STR（3d6）  ：{0}
CON（3d6）  ：{1}
POW（3d6）  ：{2}
DEX（3d6）  ：{3}
APP（3d6）  ：{4}
SIZ（2d6+6）：{5}
INT（2d6+6）：{6}
EDU（3d6+3）：{7}
--------------------
SAN（POWx5）    ：{8}
幸運（POWx5）   ：{9}
アイデア（INTx5）   ：{10}
知識（EDUx5）       ：{11}
耐久力（CON+SIZ /2）：{12}
--------------------
職業P（EDUx20） ：{13}
興味P（INTx10） ：{14}
```"""

Guide = """```\
（※ xx や yy は半角数値）

- 「@ダイス君」
    - このガイドを表示します

- 文章中に「xxdyy!」
    - 結果に置き換えて表示します
- 「CCBxx」
    - xxは技能値。成否判定とクリティカル／ファンブルが出ます

- 「/coc」
    - CoC第6版のルールでキャラシを作成します
- 「/tokucho」
    - 特徴表に沿ってダイスロールを行います
- 「/secret」
    - D100でシークレットダイスを振ります

- 「/yesno」
    - YesかNoか画像で返します
- 「/omikuji」
    - 今日の運勢を占ってみましょう！

- 「!aaa bbb ccc」
    - aaaなどは好きな文字。
      半角スペース区切りで、書かれたものの中から1つ選びます
      （例: !りんご バナナ みかん）\
```"""

emoji_list = [
    "\N{GRINNING FACE}",
    "\N{GRINNING FACE WITH SMILING EYES}",
    "\N{SMILING FACE WITH OPEN MOUTH}",
    "\N{SMILING FACE WITH OPEN MOUTH AND SMILING EYES}",
    "\N{SMILING FACE WITH OPEN MOUTH AND TIGHTLY-CLOSED EYES}",
    "\N{WINKING FACE}",
    "\N{SMILING FACE WITH SMILING EYES}",
    "\N{FACE SAVOURING DELICIOUS FOOD}",
    "\N{SMILING FACE WITH SUNGLASSES}",
    "\N{SMIRKING FACE}"
]

omikuji = [
    "願いが叶う。しかし欲張ってはいけません",
    "とても良い。現状維持を目指しなさい",
    "これから良くなる。諦めなければ吉",
    "いずれ良くなる。気長に待ちなさい",
    "問題ない。当面は安心して良いでしょう",
    "ささやかな幸せを大切にしましょう。感謝を怠らなければ吉",
    "運勢はこのまま停滞しそうです。むやみに運気上昇を願ってはいけません",
    "今の運勢は良くないが、徐々に良くなる可能性があります。不用意な発言には気をつけましょう",
    "徐々に良くなるが、期待しすぎると損をします",
    "このままだと運気は下がります。行動する際は確認を怠らないようにしなさい",
    "むやみに行動せず、嵐が過ぎるのを待ちなさい",
]

unsei = [
    "◎",
    "◎",
    "◯",
    "◯",
    "◯",
    "△",
    "△",
    "✕"
]

tokucho = [
    0,
    [
        1,
        [
            "風邪を引かない",
            "INT-1, CON+2"
        ],
        [
            "大きな体",
            "SIZ+1"
        ],
        [
            "素早い",
            "DEX+1。SIZが9以下の場合、DEX+2"
        ],
        [
            "オシャレ",
            "APP+1"
        ],
        [
            "天才",
            "INT+1"
        ],
        [
            "強固な意志",
            "正気度ポイント+5"
        ],
        [
            "勉強家",
            "EDU+1"
        ],
        [
            "幸運のお守り",
            "お守りを持っている限りPOW+1。なくすとPOW-1。正気度は変更なし"
        ],
        [
            "一族伝来の宝物",
            "アーティファクト1個所持"
        ],
        [
            "予期せぬ協力者",
            "忠誠を尽くす協力者が居る。影響力はD100（高いほど影響力が強い）"
        ]
    ],
    [
        2,
        [
            "手先が器用",
            "任意の＜制作＞成功率+50%。＜機械修理＞＜電気修理＞に+10%"
        ],
        [
            "影が薄い",
            "＜忍び歩き＞＜隠れる＞+20%"
        ],
        [
            "親の七光り",
            "＜信用＞+20%"
        ],
        [
            "愛読家",
            "＜図書館＞+20%。自宅で＜図書館＞ロール可能"
        ],
        [
            "鋭い洞察力",
            "目星+30%"
        ],
        [
            "アウトドア派",
            "＜ナビゲート＞＜博物学＞＜追跡＞+20%"
        ],
        [
            "珍しい技能",
            "INT×5%の役に立ちにくい技能を持っている"
        ],
        [
            "芸術的才能",
            "任意の＜芸術＞にINT×3%"
        ],
        [
            "バイリンガル",
            "最大3つの＜他の言語＞にEDU×5%"
        ],
        [
            "前職",
            "EDU×3%を前職の技能に割り振る"
        ]
    ],
    [
        3,
        [
            "天気予報士",
            "＜アイデア＞に成功すれば1D6+1時間の正確な天気を予想できる"
        ],
        [
            "プロドライバー",
            "あらゆる＜運転＞技能50%"
        ],
        [
            "飛ばし屋",
            "あらゆる＜操縦＞技能50%"
        ],
        [
            "戦士",
            "あらゆる近接戦闘武器の成功率50%"
        ],
        [
            "銃火器の達人",
            "拳銃、サブマシンガン、ショットガン、マシンガン、ライフルの成功率50%"
        ],
        [
            "格闘センスの持ち主",
            "キック、組み付き、頭突きの成功率50%"
        ],
        [
            "俊敏",
            "＜回避＞の成功率DEX×5"
        ],
        [
            "信頼のおける人",
            "身内を見捨てない限り任意のコミュニケーション技能3つに各+10%"
        ],
        [
            "スポーツ万能",
            "1つの技能に+20%、3つの技能に+10%"
        ],
        [
            "平凡な容姿",
            "＜変装＞+20%"
        ]
    ],
    [
        4,
        [
            "目付きが悪い",
            "知り合い以外から怖がられる。APP-1、＜信用＞-10%\n（ただし1d6 × 10の技能ポイントを得る）"
        ],
        [
            "方向音痴",
            "＜ナビゲート＞成功率1%、成長不可\n（ただし1d6 × 10の技能ポイントを得る）"
        ],
        [
            "異性が苦手",
            "異性に対する＜言いくるめ＞＜説得＞＜信用＞-10%\n（ただし1d6 × 10の技能ポイントを得る）"
        ],
        [
            "動物に嫌われる",
            "たいていの動物に威嚇される\n（ただし1d6 × 10の技能ポイントを得る）"
        ],
        [
            "不思議ちゃん",
            "多重人格？\n（ただし1d6 × 10の技能ポイントを得る）"
        ],
        [
            "寄せ餌",
            "怪物に好かれやすい\n（ただし1d6 × 10の技能ポイントを得る）"
        ],
        [
            "メガネをかけている",
            "メガネがなくなると視覚系技能最大-20%\n（ただし1d6 × 10の技能ポイントを得る）"
        ],
        [
            "大切なもの",
            "大切なものを失った際、1/1D8\n（ただし1d6 × 10の技能ポイントを得る）"
        ],
        [
            "暗黒の祖先",
            "D100の数値でヤバい祖先を決める\n（ただし1d6 × 10の技能ポイントを得る）"
        ],
        [
            "夜に弱い",
            "0時をすぎると＜アイデア＞＜知識＞の成功率が半減（端数切り上げ）\n（ただし1d6 × 10の技能ポイントを得る）"
        ]
    ],
    [
        5,
        [
            "動物に好かれる",
            "たいていの動物に好かれる"
        ],
        [
            "斜め上からの発想",
            "狂気に陥った場合、真実を見抜ける。クライマックス以外では使えない"
        ],
        [
            "失敗は発明の母",
            "96以上の出目で経験ロール。成功すれば+1ポイント"
        ],
        [
            "ペット",
            "シナリオとシナリオの間で1D3増加可能"
        ],
        [
            "おおらか",
            "精神科クリニックや診療所での正気度回復に+1"
        ],
        [
            "異物への耐性",
            "毒（POT）の抵抗に+20%"
        ],
        [
            "潜水の名人",
            "窒息に対するCONロールに+20%"
        ],
        [
            "大酒飲み",
            "すべてのアルコール関連のPOTを2分の1（端数切り上げ）にする"
        ],
        [
            "ど根性",
            "抵抗表を使用したロールに+5%"
        ],
        [
            "受け身",
            "ショックのCONロールに+20%"
        ]
    ],
    [
        6,
        [
            "奇妙な幸運",
            "神話の神性や怪物がランダムに目標を攻撃する際、対象外。ただし、単独で攻撃されたり攻撃範囲内に居た場合は対象内"
        ],
        [
            "投擲の才能",
            "＜投擲＞のダメージボーナスが通常のダメージボーナスになる"
        ],
        [
            "鋼の筋力",
            "ダメージボーナスが一段階上がる、1D6の場合、1D6+1"
        ],
        [
            "実は生きていた",
            "死からの生還チャンスが5ラウンド以内"
        ],
        [
            "急所を見抜く",
            "貫通の確率が2分の1。最大40%"
        ],
        [
            "急速な回復力",
            "耐久力を回復するロールに+1"
        ],
        [
            "不屈の精神力",
            "気絶時、各ラウンド最初にCON×2。成功するとそのラウンドから行動可能"
        ],
        [
            "マニア・コレクター",
            "任意のコレクションを収集している。＜幸運＞成功で相手に共感が得られる"
        ],
        [
            "行方不明の家族",
            "行方不明の家族が居る"
        ],
        [
            "好意を寄せられている",
            "シナリオ中の誰かに好意を持たれる。好意の強さはD100"
        ]
    ]
]

touhou_character = [
    "魂魄 妖夢",
    "霧雨 魔理沙",
    "博麗 霊夢",
    "古明地 こいし",
    "フランドール・スカーレット",
    "十六夜 咲夜",
    "レミリア・スカーレット",
    "藤原 妹紅",
    "古明地 さとり",
    "西行寺 幽々子",
    "射命丸 文",
    "アリス・マーガトロイド",
    "東風谷 早苗",
    "鈴仙・優曇華院・イナバ",
    "比那名居 天子",
    "八雲 紫",
    "秦 こころ",
    "チルノ",
    "パチュリー・ノーレッジ",
    "多々良 小傘",
    "ルーミア",
    "洩矢 諏訪子",
    "四季映姫・ヤマザナドゥ",
    "豊聡耳 神子",
    "風見 幽香",
    "純狐",
    "紅 美鈴",
    "犬走 椛",
    "鬼人 正邪",
    "依神紫苑",
    "伊吹 萃香",
    "稀神 サグメ",
    "物部 布都",
    "ヘカーティア・ラピスラズリ",
    "蓬莱山 輝夜",
    "河城 にとり",
    "八雲 藍",
    "宇佐見 蓮子",
    "霊烏路 空",
    "水橋 パルスィ",
    "茨木 華扇",
    "摩多羅隠岐奈",
    "封獣 ぬえ",
    "天弓 千亦",
    "埴安神 袿姫",
    "鍵山 雛",
    "聖 白蓮",
    "八意 永琳",
    "村紗 水蜜",
    "火焔猫 燐",
    "ドレミー・スイート",
    "クラウンピース",
    "上白沢 慧音",
    "菅牧 典",
    "マエリベリー・ハーン",
    "飯綱丸 龍",
    "吉弔 八千慧",
    "宇佐見 菫子",
    "霍 青娥",
    "姫虫 百々世",
    "大妖精",
    "橙",
    "赤蛮奇",
    "ナズーリン",
    "因幡 てゐ",
    "今泉 影狼",
    "小悪魔",
    "庭渡 久侘歌",
    "本居 小鈴",
    "星熊 勇儀",
    "ミスティア・ローレライ",
    "小野塚 小町",
    "少名 針妙丸",
    "永江 衣玖",
    "蘇我 屠自古",
    "八坂 神奈子",
    "秋 静葉",
    "姫海棠 はたて",
    "杖刀偶 磨弓",
    "森近 霖之助",
    "依神女苑",
    "二ッ岩 マミゾウ",
    "ルナサ・プリズムリバー",
    "リグル・ナイトバグ",
    "魅魔",
    "稗田 阿求",
    "堀川 雷鼓",
    "秋 穣子",
    "豪徳寺 ミケ",
    "驪駒 早鬼",
    "綿月 依姫",
    "宮古 芳香",
    "リリーホワイト",
    "奥野田 美宵",
    "メディスン・メランコリー",
    "黒谷 ヤマメ",
    "丁礼田舞",
    "神綺",
    "寅丸 星",
    "高麗野あうん",
    "わかさぎ姫",
    "岡崎 夢美",
    "幽谷 響子",
    "レティ・ホワイトロック",
    "玉造 魅須丸",
    "爾子田里乃",
    "九十九 弁々",
    "綿月 豊姫",
    "清蘭",
    "易者",
    "雲居 一輪",
    "スターサファイア",
    "ルナチャイルド",
    "メルラン・プリズムリバー",
    "幻月",
    "九十九 八橋",
    "アリスの人形",
    "リリカ・プリズムリバー",
    "山城 たかね",
    "名無しの本読み妖怪",
    "鈴瑚",
    "エタニティラルバ",
    "サニーミルク",
    "レイセン",
    "矢田寺成美",
    "カナ・アナベラル",
    "坂田ネムノ",
    "夢月",
    "蓬莱人形ジャケットイラストの娘",
    "夢子",
    "抗鬱薬おじさん",
    "牛崎 潤美",
    "くるみ",
    "魂魄 妖忌",
    "サリエル",
    "北白河 ちゆり",
    "駒草 山如",
    "キスメ",
    "毛玉",
    "雲山",
    "戎 瓔花",
    "エレン",
    "コンガラ",
    "エリス",
    "マイ",
    "ユキ",
    "エリー",
    "カワウソ霊",
    "影華扇",
    "大ナマズ",
    "るーこと",
    "UFO",
    "小兎姫",
    "蓬莱人形レーベルイラストの娘",
    "里香",
    "旧作名無し中ボス",
    "明羅",
    "レイラ・プリズムリバー",
    "オレンジ",
    "妖精",
    "朝倉 理香子",
    "玄爺",
    "核熱造神ヒソウテンソク",
    "ユウゲンマガン",
    "嫦娥",
    "ルイズ",
    "シンギョク",
    "ツチノコ",
    "ミミちゃん",
    "なめえもん",
    "チュパカブラ",
    "オオワシ霊",
    "カラス",
    "サラ",
    "キクリ",
    "オオカミ霊",
    "華扇の動物",
    "里の人間",
    "龍",
    "河童",
    "兎",
    "酒虫",
    "狐",
    "都市伝説の怪異",
    "ホフゴブリン",
    "ケセランパサラン",
    "岩笠",
    "天狗",
    "命蓮",
    "万歳楽",
    "木花咲耶姫",
    "神降ろしの神霊",
    "幽霊",
    "塩屋敷の旦那",
    "運松",
    "月の都の門番",
    "ウワバミ",
    "毘沙門天",
    "仙台四郎",
    "ヤマネ",
    "小鈴の両親",
    "狸",
    "座敷童",
    "水江浦島子",
    "煙々羅",
    "沓頬"
]

uso = [
    "ニュース(NEWS)という単語はN(北)E(東)W(西)S(南)からきている",
    "つまようじのミゾは折って『つまようじ置き』にするためにある",
    "『株式会社サンリオ』の社名は山梨県出身の創業者が『山梨の王になりたい』と『山梨王』と名付けたことからきている",
    "ヤクルトスワローズの前身国鉄スワローズは『国鉄コンドルズ』の予定だったが『混んどるズ』になるため『座ろうズ』にした",
    "サイン色紙は『表側に書く程の者ではない』と謙遜する意味で裏側の白い面に書いている",
    "つむじを押すと下痢になる",
    "『ぐっすり』は『Good Sleep』からきている",
    "外科医には『手術中トイレに行かなくていいようにオムツを履いておく』という決まりがある",
    "木の年輪で東西南北がわかる",
    "スイートルームとは新婚夫婦が泊まる甘いムードの部屋という意味",
    "『104』の番号案内はすべて沖縄県で行っている",
    "回転寿司のお寿司が回る速度は関東よりも関西の方が速い",
    "『CDを冷やすと音質が良くなる』",
    "舌の甘味や苦味を感じる場所はそれぞれ完全に分かれている",
    "爪の半月が小さいと不健康",
    "洗面所の栓を抜くと出来る渦は北半球では左回りで南半球では右回り",
    "ウサギは一匹だけでいると寂しくて死ぬ",
    "ネコはヒゲの幅より狭い場所は通れない",
    "トイレットペーパーを何回折っても大腸菌は通り抜ける",
    "体脂肪が燃焼するのは運動開始20分後から",
    "理髪店のサインポールは赤が動脈青が静脈を表している",
    "白髪は抜くと増える",
    "スイカの種を飲み込むと盲腸になる",
    "ペットボトルに水を入れて置いておくとネコよけになる",
    "卵は白より茶色の方が高級",
    "世界の標準時間はイギリスのグリニッジ天文台が決めている",
    "時代劇『水戸黄門』でうっかり八兵衛は『黄門様ファイト』と言ってしまった事がある",
    "ベースボールを『野球』と名付けたのは正岡子規",
    "自由の女神の視線の先には送り主のフランスがある",
    "ジンギスカンはモンゴル民族が兜で肉を焼き始めたのが起源",
    "ハチに刺されたらおしっこをかけて消毒するのが良い",
    "ダイアル『119』は緊急時心を落ち着かせる為末尾をゆっくり戻る『9』にしてある",
    "九州の方言で『しかし』を意味する『ばってん』は英語の『But then』からきている",
    "サッカーの試合中に興奮した選手がボールを持って走ったことからラグビーが生まれた",
    "富士の樹海の中では方位磁石が効かない",
    "カテキンは『勝て菌』から名付けられた",
    "孫悟空のモデルとなったサルは中国の猿『キンシコウ』",
    "結婚式のご祝儀で一万円札を奇数枚にするのは割り切れる偶数だと『別れる』という意味になるため",
    "『豆腐』と『納豆』は意味と漢字が逆に伝わっている",
    "焼肉の『ホルモン』は関西弁で『捨てる物』を意味する『放るもん』が語源",
    "フグの刺身が薄いのは高級なものを少しでも長く味わえるようにするため",
    "寿司屋でお茶を『あがり』と呼ぶのは食事の締めに飲むものだから",
    "ネコは自分の死を悟ると死に場所を求めて姿を消す",
    "牛は赤い物を見ると興奮する"
]
