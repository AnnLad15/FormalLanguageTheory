\documentclass[a4paper, 14pt]{extarticle}
\usepackage{forest} 
\usepackage{qtree}

% Поля
%--------------------------------------
\usepackage{geometry}
\geometry{a4paper,tmargin=2cm,bmargin=2cm,lmargin=3cm,rmargin=1cm}
%--------------------------------------


%Russian-specific packages
%--------------------------------------
\usepackage[T2A]{fontenc}
\usepackage[utf8]{inputenc} 
\usepackage[english, main=russian]{babel}
%--------------------------------------

\usepackage{textcomp}

% Красная строка
%--------------------------------------
\usepackage{indentfirst}               
%--------------------------------------             


%Graphics
%--------------------------------------
\usepackage{graphicx}
\graphicspath{ {./images/} }
\usepackage{wrapfig}
%--------------------------------------

% Полуторный интервал
%--------------------------------------
\linespread{1.3}                    
%--------------------------------------

%Выравнивание и переносы
%--------------------------------------
% Избавляемся от переполнений
\sloppy
% Запрещаем разрыв страницы после первой строки абзаца
\clubpenalty=10000
% Запрещаем разрыв страницы после последней строки абзаца
\widowpenalty=10000
%--------------------------------------

%Списки
\usepackage{enumitem}

%Подписи
\usepackage{caption} 

%Гиперссылки
\usepackage{hyperref}

\hypersetup {
	unicode=true
}

%Рисунки
%--------------------------------------
\DeclareCaptionLabelSeparator*{emdash}{~--- }
\captionsetup[figure]{labelsep=emdash,font=onehalfspacing,position=bottom}
%--------------------------------------

\usepackage{tempora}

%Листинги
%--------------------------------------
\usepackage{listings}
\lstset{
  basicstyle=\ttfamily\footnotesize, 
  %basicstyle=\footnotesize\AnkaCoder,        % the size of the fonts that are used for the code
  breakatwhitespace=false,         % sets if automatic breaks shoulbd only happen at whitespace
  breaklines=true,                 % sets automatic line breaking
  captionpos=t,                    % sets the caption-position to bottom
  inputencoding=utf8,
  frame=single,                    % adds a frame around the code
  keepspaces=true,                 % keeps spaces in text, useful for keeping indentation of code (possibly needs columns=flexible)
  keywordstyle=\bf,       % keyword style
  numbers=left,                    % where to put the line-numbers; possible values are (none, left, right)
  numbersep=5pt,                   % how far the line-numbers are from the code
  xleftmargin=25pt,
  xrightmargin=25pt,
  showspaces=false,                % show spaces everywhere adding particular underscores; it overrides 'showstringspaces'
  showstringspaces=false,          % underline spaces within strings only
  showtabs=false,                  % show tabs within strings adding particular underscores
  stepnumber=1,                    % the step between two line-numbers. If it's 1, each line will be numbered
  tabsize=2,                       % sets default tabsize to 8 spaces
  title=\lstname                   % show the filename of files included with \lstinputlisting; also try caption instead of title
}
%--------------------------------------

%%% Математические пакеты %%%
%--------------------------------------
\usepackage{amsthm,amsfonts,amsmath,amssymb,amscd}  % Математические дополнения от AMS
\usepackage{mathtools}                              % Добавляет окружение multlined
\usepackage[perpage]{footmisc}
%--------------------------------------

%--------------------------------------
%			НАЧАЛО ДОКУМЕНТА
%--------------------------------------

\begin{document}

%--------------------------------------
%			ТИТУЛЬНЫЙ ЛИСТ
%--------------------------------------
\begin{titlepage}
\thispagestyle{empty}
\newpage


%Шапка титульного листа
%--------------------------------------
\vspace*{-60pt}
\hspace{-65pt}
\begin{minipage}{0.3\textwidth}
\hspace*{-20pt}\centering
\includegraphics[width=\textwidth]{emblem}
\end{minipage}
\begin{minipage}{0.67\textwidth}\small \textbf{
\vspace*{-0.7ex}
\hspace*{-6pt}\centerline{Министерство науки и высшего образования Российской Федерации}
\vspace*{-0.7ex}
\centerline{Федеральное государственное бюджетное образовательное учреждение }
\vspace*{-0.7ex}
\centerline{высшего образования}
\vspace*{-0.7ex}
\centerline{<<Московский государственный технический университет}
\vspace*{-0.7ex}
\centerline{имени Н.Э. Баумана}
\vspace*{-0.7ex}
\centerline{(национальный исследовательский университет)>>}
\vspace*{-0.7ex}
\centerline{(МГТУ им. Н.Э. Баумана)}}
\end{minipage}
%--------------------------------------

%Полосы
%--------------------------------------
\vspace{-25pt}
\hspace{-35pt}\rule{\textwidth}{2.3pt}

\vspace*{-20.3pt}
\hspace{-35pt}\rule{\textwidth}{0.4pt}
%--------------------------------------

\vspace{1.5ex}
\hspace{-35pt} \noindent \small ФАКУЛЬТЕТ\hspace{80pt} <<Информатика и системы управления>>

\vspace*{-16pt}
\hspace{47pt}\rule{0.83\textwidth}{0.4pt}

\vspace{0.5ex}
\hspace{-35pt} \noindent \small КАФЕДРА\hspace{50pt} <<Теоретическая информатика и компьютерные технологии>>

\vspace*{-16pt}
\hspace{30pt}\rule{0.866\textwidth}{0.4pt}
  
\vspace{11em}

\begin{center}
\Large {\bf Лабораторная работа №1} \\ 
\large {\bf по курсу <<Теория формальных языков>>} \\ 
\end{center}\normalsize

\vspace{8em}


\begin{flushright}
  {Студент группы ИУ9-52Б Ладонцева А.А. \hspace*{15pt}\\ 
  \vspace{2ex}
  Преподаватель: Непейвода А.Н.\hspace*{15pt}}
\end{flushright}

\bigskip

\vfill
 

\begin{center}
\textsl{Москва 2025}
\end{center}
\end{titlepage}
%--------------------------------------
%		КОНЕЦ ТИТУЛЬНОГО ЛИСТА
%--------------------------------------

\renewcommand{\ttdefault}{pcr}

\setlength{\tabcolsep}{3pt}
\newpage
\setcounter{page}{2}



\tableofcontents


\newpage


\section{Постоновка задачи}\label{Sect::res}



\newpage
\section{Индивидуальный вариант №14}\label{Sect::res}
1) $ac \to c$ 

2) $aa \to ba$

3) $bc \to c$

4) $ca \to aa$

5) $cb \to bc$

6) $ccc \to c$

7) $aaa \to aa$

8) $aab \to ba$

9) $abb \to aba$

10) $bbb \to bba$


\section{Доказательство завершимости}\label{Sect::res}
У нас есть алфавит {a, b, c} и 10 правил вида u → v, где u и v — строки.
SRS завершима (terminating), если не существует бесконечной последовательности переписываний, т.е. любой процесс рано или поздно останавливается.

Сначала проверим, всегда ли длина строки уменьшается.

Длина уменьшается в правилах:

1) ac → c (2 → 1)

3) bc → c (2 → 1)

6) ccc → c (3 → 1)

7) aaa → aa (3 → 2)

8) aab → ba (3 → 2)

Длина сохраняется в правилах:

2) aa → ba (2 → 2)

4) ca → aa (2 → 2)

5) cb → bc (2 → 2)

9) abb → aba (3 → 3) 

10) bbb → bba (3 → 3)

Правил, где длина увеличивается, нету.

Теперь пройдемся более подробно по каждому правилу. 

Шаг 1. 

Рассмотрим правила 1) ac → c и 3) bc → c .

Из этих двух правил следует, что если перед буквой $\bm{c}$ встретились буква $\bm{a}$ или $\bm{b}$ , то они пропадут , а $\bm{c}$ останется в неизменном виде. Длинна слова уменьшается. поэтому оба этих правила приведут к конечному результату. 
size(t)>size(t')

\vspace{1cm} 

Шаг 2.
Рассмотрим правила 3) bc → c и 5) cb → bc .

Правило 5) дополняет правило 3) и сново сводит его к результату $\bm{c}$.

$w_1$bc$w_2$ -> $w_1$c$w_2$

$w_1$cb$w_2$ -> $w_1$bc$w_2$-> $w_1$c$w_2$

\vspace{1cm}

Шаг 3.

Рассмотрим правило 6) ccc → c.

$size(t)_c$ > $size(t')_c$  (3>1)

При получении длинной последовательности состоящей из $\bm{c}$, можем сократить их количество в 2/3 раза и сводит результат к $\bm{c}$.


\vspace{1cm}

Шаг 4.
Рассмотрим правила 1) ac → c и 4) ca → aa.

Какую бы пару не встретили всегда есть для нее правило, которое в любом случае избавляет от одной буквы ( не в значении кол-ва ).

Рассмотрим пример (построить нормальные деревья потом)




Из примера можно сделать вывод:
а) если перед "c" есть "a", то рано или поздно придем к последовательности состоящий из "c" ( в кол-ве от 1 до N штук). 
b) Если "a" стоит после "c", то все "c" превращаются в "a".



\vspace{1cm}

Шаг 5.

Рассмотрим правило 7) aaa → aa в дополнение к прошлому шагу. 

Оно уменьшает кол-во "a"  и поэтому ускоряет процесс уменьшения слова. (подходит для пункта b) из шага 4)

$size(t)_a$ > $size(t')_a$  (3>2)


\vspace{1cm}

Шаг 6.

Рассмотрим оставшиеся правила, а именно:
2) aa → ba 

8) aab → ba

9) abb → aba  

10) bbb → bba 

Первые да правила сводятся к одному результату.

Вторые два правила дают разный результат, но у обоих результат зависит от первой буквы. 

Можно заметить, что у нас нет правила содержащего буквы "a" и "b", где "b" была бы первой. Здесь можно зделать пометку, что если мы дойдем до такой комбинации, то она будет конечна (не для всех случаев. Только если длина слова меньше или ровна 3)

Рассмотрим для примера все слова длины 3, состоящие только из букв a и b.

\Tree [.aaa [.aa ba ] ] 
\Tree [.aab ba ]
\Tree [.aba ]
\Tree [.abb aba ]

\vspace{1cm}

\Tree [.baa bba ]
\Tree [.bab ]
\Tree [.bba ]
\Tree [.bbb bba ]


Проведя серию применений правил к различным словам, я нашла комбинации букв, слова состоящие из которые будут конечны:
ba, bba, aba, (и еще возможно ab) 

Если рассматривать случае на более длинных словах, то результат снова сводится к выше указанным комбинациям.




Из всех рассмотренных шагов, можно сделать вывод, что SRS завершима. 





\section{Доказательство конечности}\label{Sect::res}
1) ac  <-> c

2) aa  <-> ba

3) bc  <-> c

4) ca  <-> aa

5) cb  <-> bc

6) ccc <-> c

7) aaa <-> aa

8) aab <-> ba

9) abb <-> aba

10) bbb <-> bba


Некоторые полезные следствия, которые сразу видны из правил:

\begin{itemize}
    \item ac <-> c и bc <-> c ⇒ буква перед c если это a или b может «исчезнуть» (например ac → c, bc → c). Обратная замена c → ac или c → bc тоже возможна.


    \item cb <-> bc вместе с bc <-> c даёт cb эквивалентно c (через cb -> bc -> c).

    \item ccc <-> c сокращает три подряд c до одного c. Значит большие блоки c сокращаются по модулю 2? (не совсем, но тройки сворачиваются).

    \item ca <-> aa превращает c слева от a в aa (может как увеличивать, так и менять буквы).

    \item aaa <-> aa и aa <-> ba и aab <-> ba дают много тождеств между длинными блоками a и сочетаниями с b: блоки a сворачиваются до длины ≤2 (с помощью aaa->aa), но aa и ba эквивалентны и взаимно переставляемы — т.е. b и a могут «замещать» друг друга местами.

\end{itemize}

Проведем эксперимент. 

Для всех слов длины ≤ 5 (в алфавите {a,b,c}) я построила множество слов, эквивалентных каждому слову. В этом ограниченном эксперименте получилось, что все слова длины ≤5 приводятся (в пределах поиска) к конечному набору «репрезентантов». Набор репрезентантов — следующий:
a, aa, ab, ac, b, bb, bc, c, ca. 

Исходя из исходных правил и найденных представителей, можно предложить ориентированную систему переписываний (правила «в сторону нормальной формы»), которая делает попытку редуцировать каждое слово к одному из найденных репрезентантов.

Ориентированные правила:

ac  -> c

bc  -> c

cb  -> c (через cb->bc и bc->c; записано как непосредственное редуцирование)

ccc -> c

aaa -> aa

aab -> ba

aa  -> aa  (оставляем aa фиксированной нормальной формой для «a-блоков»)

ca  -> aa

abb -> aba    (оставляем, если это снижает лексикографию) 

bbb -> bba

Это не окончательно доказывает конечность, а лишь дает предпосылки, что система конечна. Для окончательного докозательства, рассмотрим следующий пункт. 



\section{Определение локальной конфлюэнтности и пополняемость по Кнуту-Бендиксу}\label{Sect::res}

Для начала был выбран фундированный порядок c > a > b.

Затем упорядочены правила сначала по правилу shortlexу (равнение по длине), затем лексикографически. 

1) ac -> c 

2) aa -> ba 

3) bc -> c 

4) ca -> aa 

5) cb -> bc 

6) ccc -> c 

7) aaa -> aa 

8) aab -> ba 

9) aba -> abb 

10) bba -> bbb

Вданном случае переписались правила 9) и 10).

Дальше приминила алгоритм пополняемость по Кнуту-Бендиксу. 

Ниже преведены примеры при которых были получины новые правила. 
Более подробный вариант, в котором рассписаны все случае смотрить в отдельном файле. (там фотографии ручного способа )

(4)(1) 
\Tree [.cac [.bac [.bc c ] ] cc ] 

11) cc -> c

\vspace{1cm}

(2)(2) 
\Tree [.aaa [.baa [.bba bbb ] ] [.aba abb ] ] 

12) abb -> bbb

\vspace{1cm}

(4)(2)
\Tree [.caa [.aaa [.aa ba ] ] [.cda [.baa [.bba bbb ] ] ] ] 

13) bbb -> ba

\vspace{1cm}

(7)(2)
\Tree [.aaaa [.aaa [.aa ba ] ] [.aaba [.baba [.babb [.bbbb bab ] ] ] ] ] 

14) bab -> ba

\vspace{1cm}

(5)(10)
\Tree [.bcba [.cba [.bca [.baa [.bba [.bbb ba ] ] ] ] ] [.cbbb [.bcbb [.cbb [.bcb [.cb [.bc c ] ] ] ] ] ] ] 

15) ba -> c

После получения ba -> c многие критические пары уже редуцировались к одному общему нормальному виду, поэтому дальнейших новых правил уже не появлялось.

\vspace{1cm}

Получили пять новых правил. Я просчитывала критические пары пока не переставали появляться новые правила. Далее, используя полученный набор правил для редукции слов, большинство слов сводится к небольшому множест­ву нормальных форм: a, b, c, ab, bb. 

1) ac -> c 

2) aa -> ba -> c

3) bc -> c 

4) ca -> aa -> ba -> c

5) cb -> bc -> c

6) ccc -> c 

7) aaa -> aa -> ba -> c

8) aab -> ba -> c

9) aba -> abb -> bbb -> ba -> c

10) bba -> bbb -> ba -> c

11) cc -> c

12) abb -> bbb -> ba -> c

13) bbb -> ba -> c

14) bab -> ba -> c

15) ba -> c


Окончательная минимизированная (практическая) система правил:
aa -> c

ac -> c

ba -> c

bc -> c

cb -> c

cc -> c

Критические пары разрешаются, т.е. система локально конфлюэнтна. 
Отсюда вытекает и конечность. 

\end{document}
