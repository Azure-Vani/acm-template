 #-*- encoding: utf-8 -*-

import os

remark="remark.tex"
main = ""

def dfs(level, path):
    global main
    if os.path.isfile(path + '/' + remark):
        i = path + '/' + remark
        main += "\\input{%s}\n"%(i)
    for i in os.listdir(path):
        j = i
        i = path + '/' + i
        if (os.path.isdir(i) and i != "./.git"):
            main += "\\%ssection{%s}"%(level, j) + "\n"
            dfs(level + "sub", i)
        else:
            if (j == remark): continue
            else: 
                if (level != ""): main += "\\code{%s}"%(i) + "\n"

dfs("", ".")

print r"""

\documentclass[a4paper,11pt]{article}

\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{cmap}
\usepackage{geometry}
\usepackage[bookmarks=true,colorlinks,linkcolor=black]{hyperref}
\usepackage{indentfirst}
\usepackage{xeCJK}
\usepackage{titlesec}
\usepackage{fancyhdr}

\usepackage{listings} %插入代码
\usepackage{xcolor} %代码高亮

\pagestyle{fancy}
\fancyhf{}
\rhead{\thepage}
\lhead{Peking University}
 
\definecolor{mygreen}{rgb}{0,0.6,0}
\definecolor{AnswerColor}{rgb}{0.8,0,0}
\lstset{
%	xleftmargin=0.5em, xrightmargin=0.5em,aboveskip=1em,
	tabsize=4,
	basicstyle=\ttfamily\small, 
	frame=none,
	breaklines,
	extendedchars=false
	keywordstyle=\bfseries\color{black}, 
	commentstyle=\itshape\color{black}, 
	language=C++,
}

\newcommand{\code}[1]{\lstinputlisting{#1}}

\geometry{margin=1in}

\setCJKmainfont[BoldFont={Adobe Heiti Std}]{Adobe Song Std}
\setCJKfamilyfont{hei}{Adobe Heiti Std}
%\setmainfont{Times New Roman}

\title{Obsidian Team Reference}
\author{Peking University}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage
""" + main + """
\end{document}
"""

