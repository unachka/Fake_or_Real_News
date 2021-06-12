{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import datetime\n",
    "import re, string\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import dtale"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_fake = pd.read_csv(\"Fake.csv\")\n",
    "df_true = pd.read_csv(\"True.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### EDA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>text</th>\n",
       "      <th>subject</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>6624</th>\n",
       "      <td>Trump Disproves The Effectiveness Of Walls As...</td>\n",
       "      <td>Since the beginning of Donald Trump s campaign...</td>\n",
       "      <td>News</td>\n",
       "      <td>April 30, 2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11440</th>\n",
       "      <td>SHOCKER! CNN POLITICAL DIRECTOR On Trump’s Fir...</td>\n",
       "      <td></td>\n",
       "      <td>politics</td>\n",
       "      <td>Mar 11, 2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18215</th>\n",
       "      <td>DEMOCRAT HEADS SET TO EXPLODE: Feds Waive Envi...</td>\n",
       "      <td>The Department of Homeland Security announced ...</td>\n",
       "      <td>left-news</td>\n",
       "      <td>Aug 3, 2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14938</th>\n",
       "      <td>FORMER CIA AGENT SAYS OBAMA WORKING WITH MUSLI...</td>\n",
       "      <td>Former CIA Agent, Clare Lopez has been ringing...</td>\n",
       "      <td>politics</td>\n",
       "      <td>Nov 13, 2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20194</th>\n",
       "      <td>TRUMP SAYS “NO” To Pro-Amnesty Koch Brother’s ...</td>\n",
       "      <td>Meanwhile, the Koch brothers are denying they ...</td>\n",
       "      <td>left-news</td>\n",
       "      <td>Jul 30, 2016</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                   title  \\\n",
       "6624    Trump Disproves The Effectiveness Of Walls As...   \n",
       "11440  SHOCKER! CNN POLITICAL DIRECTOR On Trump’s Fir...   \n",
       "18215  DEMOCRAT HEADS SET TO EXPLODE: Feds Waive Envi...   \n",
       "14938  FORMER CIA AGENT SAYS OBAMA WORKING WITH MUSLI...   \n",
       "20194  TRUMP SAYS “NO” To Pro-Amnesty Koch Brother’s ...   \n",
       "\n",
       "                                                    text    subject  \\\n",
       "6624   Since the beginning of Donald Trump s campaign...       News   \n",
       "11440                                                      politics   \n",
       "18215  The Department of Homeland Security announced ...  left-news   \n",
       "14938  Former CIA Agent, Clare Lopez has been ringing...   politics   \n",
       "20194  Meanwhile, the Koch brothers are denying they ...  left-news   \n",
       "\n",
       "                 date  \n",
       "6624   April 30, 2016  \n",
       "11440    Mar 11, 2017  \n",
       "18215     Aug 3, 2017  \n",
       "14938    Nov 13, 2015  \n",
       "20194    Jul 30, 2016  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_fake.sample(5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"475\"\n",
       "            src=\"http://UNDRAKHs-MacBook-Air.local:40000/dtale/iframe/1\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x7fc174f27100>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": []
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dtale.show(df_fake)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>text</th>\n",
       "      <th>subject</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>13370</th>\n",
       "      <td>Cameroon secessionists kill six soldiers, poli...</td>\n",
       "      <td>YAOUNDE (Reuters) - Militants seeking independ...</td>\n",
       "      <td>worldnews</td>\n",
       "      <td>December 1, 2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15406</th>\n",
       "      <td>Chinese fans prepare to welcome rich, powerful...</td>\n",
       "      <td>BEIJING (Reuters) - He may be a divisive figur...</td>\n",
       "      <td>worldnews</td>\n",
       "      <td>November 7, 2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17752</th>\n",
       "      <td>UK government softens immigration rules for Gr...</td>\n",
       "      <td>LONDON (Reuters) - Illegal immigrants who surv...</td>\n",
       "      <td>worldnews</td>\n",
       "      <td>October 11, 2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5102</th>\n",
       "      <td>McCain calls on Trump to back up wire-tapping ...</td>\n",
       "      <td>WASHINGTON (Reuters) - U.S. Senator John McCai...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>March 6, 2017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13135</th>\n",
       "      <td>Stopping militancy spread in ASEAN a priority ...</td>\n",
       "      <td>SINGAPORE (Reuters) - Southeast Asian countrie...</td>\n",
       "      <td>worldnews</td>\n",
       "      <td>December 5, 2017</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                   title  \\\n",
       "13370  Cameroon secessionists kill six soldiers, poli...   \n",
       "15406  Chinese fans prepare to welcome rich, powerful...   \n",
       "17752  UK government softens immigration rules for Gr...   \n",
       "5102   McCain calls on Trump to back up wire-tapping ...   \n",
       "13135  Stopping militancy spread in ASEAN a priority ...   \n",
       "\n",
       "                                                    text       subject  \\\n",
       "13370  YAOUNDE (Reuters) - Militants seeking independ...     worldnews   \n",
       "15406  BEIJING (Reuters) - He may be a divisive figur...     worldnews   \n",
       "17752  LONDON (Reuters) - Illegal immigrants who surv...     worldnews   \n",
       "5102   WASHINGTON (Reuters) - U.S. Senator John McCai...  politicsNews   \n",
       "13135  SINGAPORE (Reuters) - Southeast Asian countrie...     worldnews   \n",
       "\n",
       "                    date  \n",
       "13370  December 1, 2017   \n",
       "15406  November 7, 2017   \n",
       "17752  October 11, 2017   \n",
       "5102      March 6, 2017   \n",
       "13135  December 5, 2017   "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_true.sample(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fake news dataset shape (23481, 4)\n",
      "Real news dataset shape (21417, 4)\n"
     ]
    }
   ],
   "source": [
    "print(\"Fake news dataset shape\", df_fake.shape)\n",
    "print(\"Real news dataset shape\", df_true.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 23481 entries, 0 to 23480\n",
      "Data columns (total 4 columns):\n",
      " #   Column   Non-Null Count  Dtype \n",
      "---  ------   --------------  ----- \n",
      " 0   title    23481 non-null  object\n",
      " 1   text     23481 non-null  object\n",
      " 2   subject  23481 non-null  object\n",
      " 3   date     23481 non-null  object\n",
      "dtypes: object(4)\n",
      "memory usage: 733.9+ KB\n"
     ]
    }
   ],
   "source": [
    "df_fake.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 21417 entries, 0 to 21416\n",
      "Data columns (total 4 columns):\n",
      " #   Column   Non-Null Count  Dtype \n",
      "---  ------   --------------  ----- \n",
      " 0   title    21417 non-null  object\n",
      " 1   text     21417 non-null  object\n",
      " 2   subject  21417 non-null  object\n",
      " 3   date     21417 non-null  object\n",
      "dtypes: object(4)\n",
      "memory usage: 669.4+ KB\n"
     ]
    }
   ],
   "source": [
    "df_true.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fake News\n",
      "News               9050\n",
      "politics           6841\n",
      "left-news          4459\n",
      "Government News    1570\n",
      "US_News             783\n",
      "Middle-east         778\n",
      "Name: subject, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(\"Fake News\")\n",
    "print(df_fake.subject.value_counts())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Real News\n",
      "politicsNews    11272\n",
      "worldnews       10145\n",
      "Name: subject, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "\n",
    "print(\"Real News\")\n",
    "print( df_true.subject.value_counts())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fake News\n",
      "May 10, 2017                                                                                                                                             46\n",
      "May 26, 2016                                                                                                                                             44\n",
      "May 5, 2016                                                                                                                                              44\n",
      "May 6, 2016                                                                                                                                              44\n",
      "May 11, 2016                                                                                                                                             43\n",
      "                                                                                                                                                         ..\n",
      "https://100percentfedup.com/12-yr-old-black-conservative-whose-video-to-obama-went-viral-do-you-really-love-america-receives-death-threats-from-left/     1\n",
      "October 22, 2017                                                                                                                                          1\n",
      "https://100percentfedup.com/video-hillary-asked-about-trump-i-just-want-to-eat-some-pie/                                                                  1\n",
      "Jun 7, 2015                                                                                                                                               1\n",
      "November 20, 2017                                                                                                                                         1\n",
      "Name: date, Length: 1681, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(\"Fake News\")\n",
    "print( df_fake.date.value_counts())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(df_fake['date'][1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_fake.date.str.contains(r'https://').sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_fake = df_fake[~df_fake.date.str.startswith('https://')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2021-06-12 12:41:09,072 - INFO     - NumExpr defaulting to 4 threads.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>text</th>\n",
       "      <th>subject</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>18933</th>\n",
       "      <td>Homepage</td>\n",
       "      <td>[vc_row][vc_column width= 1/1 ][td_block_trend...</td>\n",
       "      <td>left-news</td>\n",
       "      <td>MSNBC HOST Rudely Assumes Steel Worker Would N...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          title                                               text    subject  \\\n",
       "18933  Homepage  [vc_row][vc_column width= 1/1 ][td_block_trend...  left-news   \n",
       "\n",
       "                                                    date  \n",
       "18933  MSNBC HOST Rudely Assumes Steel Worker Would N...  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_fake[~(df_fake.date.str.len() <19)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_fake = df_fake[~df_fake.date.str.startswith('MSNBC HOST')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fake News\n",
      "May 10, 2017         46\n",
      "May 5, 2016          44\n",
      "May 6, 2016          44\n",
      "May 26, 2016         44\n",
      "May 11, 2016         43\n",
      "                     ..\n",
      "October 9, 2017       1\n",
      "14-Feb-18             1\n",
      "December 22, 2017     1\n",
      "December 4, 2017      1\n",
      "October 22, 2017      1\n",
      "Name: date, Length: 1675, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(\"Fake News\")\n",
    "print( df_fake.date.value_counts())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# date formating is inconssitent we need to change"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Real News\n",
      "December 20, 2017      182\n",
      "December 6, 2017       166\n",
      "November 30, 2017      162\n",
      "November 9, 2017       158\n",
      "October 13, 2017       155\n",
      "                      ... \n",
      "September 11, 2016       1\n",
      "August 21, 2016          1\n",
      "May 14, 2016             1\n",
      "June 24, 2017            1\n",
      "December 30, 2017        1\n",
      "Name: date, Length: 716, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(\"Real News\")\n",
    "print( df_true.date.value_counts())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "df_fake['date_only'] = pd.to_datetime(df_fake['date'])\n",
    "df_true['date_only'] = pd.to_datetime(df_true['date'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_fake['year'] = df_fake['date_only'].dt.year\n",
    "df_true['year'] = df_true['date_only'].dt.year\n",
    "\n",
    "df_fake['month'] = df_fake['date_only'].dt.month\n",
    "df_true['month'] = df_true['date_only'].dt.month\n",
    "\n",
    "df_fake['day'] = df_fake['date_only'].dt.day\n",
    "df_true['day'] = df_true['date_only'].dt.day\n",
    "\n",
    "df_fake['week_day'] = df_fake['date_only'].dt.weekday\n",
    "df_true['week_day'] = df_true['date_only'].dt.weekday\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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rVbJ08iRI5k+fXqrw5AkSZLUpiLi0a7WOWxPkiRJkioweZIkSZKkCkyeJEmSJKmC1eqaJ0mSJKm/WLx4MXPmzOGFF15odSgD0tChQxkxYgSDBw+uvI3JkyRJktSG5syZwytf+UpGjhxJRLQ6nAElM5k/fz5z5sxh1KhRlbdz2J4kSZLUhl544QU23HBDE6cmiAg23HDDHvfqmTxJkiRJbcrEqXlWpW1NniRJkiSpAq95kiRJkvqBkUf9pqH7m33SfiutM2jQILbbbjuWLFnCqFGj+OlPf8qwYcN6fKyzzz6b6dOn893vfncVIm0f9jxJkiRJqmvttddm5syZ3H333WywwQacccYZrQ6ppUyeJEmSJK3U2LFjmTt3LgAPPfQQ++67L6NHj2bcuHHcd999APz617/mzW9+MzvttBNvf/vbefzxxyvte9KkSRx55JHstttuvO51r+Piiy9evu6UU05hl112Yfvtt+fYY48F4OSTT+b0008H4Atf+AJve9vbAJg2bRof/vCHWbp0KZMmTWLbbbdlu+2249vf/nZD2sDkSZIkSVK3li5dyrRp0zjggAMAOOyww/jOd77DjBkzOPXUU/n0pz8NwFve8hZuueUW/vSnPzFx4kROPvnkyseYN28eN954I5dffjlHHXUUAFOnTuWBBx7gtttuY+bMmcyYMYPrr7+e8ePHc8MNNwAwffp0Fi5cyOLFi7nxxhsZN24cM2fOZO7cudx9993cddddHHrooQ1pB695kiRJklTX888/z4477sjs2bMZPXo0e+21FwsXLuSmm25iwoQJy+stWrQIKO5N9f73v5958+bx4osv9ugeSgcddBBrrLEGW2+99fIeq6lTpzJ16lR22mknABYuXMgDDzzAwQcfzIwZM3j22WcZMmQIO++8M9OnT+eGG27g9NNPZ7PNNuPhhx/miCOOYL/99mPvvfduSHuYPEmSJGlA6cnEClUmTViddVzztGDBAvbff3/OOOMMJk2axLBhw5g5c+bL6h9xxBF88Ytf5IADDuDaa69l8uTJlY81ZMiQ5c8zc/nj0UcfzSc/+cmX1R85ciRnnXUWu+22G9tvvz3XXHMNDz30EFtttRURwR133MGVV17JGWecwYUXXsiZZ57Z4/ffmcP2JEmSJHVr/fXX5/TTT+fUU09l7bXXZtSoUVx00UVAkeDccccdACxYsIDhw4cDcM455/T6uPvssw9nnnkmCxcuBGDu3Lk88cQTAIwfP55TTz2V8ePHM27cOH7wgx+w4447EhE89dRTLFu2jPe85z184xvf4Pbbb+91LGDPkyRJktQvtLqXbKeddmKHHXbgggsu4Pzzz+fwww/nhBNOYPHixUycOJEddtiByZMnM2HCBIYPH86uu+7KI4880qtj7r333syaNYuxY8cCsO6663LeeeexySabMG7cOKZMmcLYsWNZZ511GDp0KOPGjQOKJOvQQw9l2bJlAJx44om9e/Ol6OgSWx2MGTMmp0+f3uowJEmS1EQDZdjerFmz2GqrrVodxoBWr40jYkZmjqlX32F7kiRJklSBw/YkSZIk9YkpU6Ysv1aqw4QJEzjmmGNaFFHPmDxJkiRJ6hPHHHNMv0mU6nHYniRJkiRVYPIkSZIkSRU4bE+SJEnqhZ7M7gftPcOfumfPkyRJkiRVYM+TJEmS1B9MXr/B+1uw0iqDBg1iu+22W/76kksuYeTIkS+rN3v2bPbff3/uvvvuRkbYdkyeJEmSJNW19tprM3PmzFaH0TYctidJkiSpkoULF7Lnnnuy8847s91223HppZe+rM7DDz/MTjvtxB//+Eceeugh9t13X0aPHs24ceO47777utz3pEmTOPLII9ltt9143etex8UXX7x83SmnnMIuu+zC9ttvz7HHHgvAySefzOmnnw7AF77wBd72trcBMG3aND784Q+zdOlSJk2axLbbbst2223Ht7/97V6/f3ueJEmSJNX1/PPPs+OOOwIwatQoLrroIn71q1+x3nrr8dRTT7HrrrtywAEHLK9///33M3HiRM466yx23HFH9txzT37wgx+w5ZZbcuutt/LpT3+aq6++usvjzZs3jxtvvJH77ruPAw44gPe+971MnTqVBx54gNtuu43M5IADDuD6669n/PjxfPOb3+TII49k+vTpLFq0iMWLF3PjjTcybtw4Zs6cydy5c5cPJXzmmWd63R4mT5IkSZLq6jxsb/HixXz1q1/l+uuvZ4011mDu3Lk8/vjjADz55JMceOCB/OIXv2CbbbZh4cKF3HTTTUyYMGH59osWLer2eAcddBBrrLEGW2+99fL9Tp06lalTp7LTTjsBRe/XAw88wMEHH8yMGTN49tlnGTJkCDvvvDPTp0/nhhtu4PTTT2ezzTbj4Ycf5ogj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\n",
      "text/plain": [
       "<Figure size 1008x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.show()\n",
    "\n",
    "true = (df_true['date_only'])\n",
    "fake = (df_fake['date_only'])\n",
    "\n",
    "plt.figure(figsize = (14,6))\n",
    "plt.title(\"Distribution of Publication Date\", fontsize=20)\n",
    "plt.hist([true, fake], bins = 25)\n",
    "plt.legend([\"Real_news\", \"Fake_news\"])\n",
    "plt.ylabel(\"Number of News Released\", fontsize=16)\n",
    "plt.xlabel(\"Year - Date\",fontsize=16)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Here we can tell that Fake news dates are more evently distrubuted and real news happened more in to 2017 to 2018"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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mblBvbqVKnkaMmQIkydPbnYYkiRJklpURDzTUZ3D9iRJkiSpApMnSZIkSarA5EmSJEmSKlip5jxJkiRJy4sFCxYwY8YMXn/99WaHskLq27cvgwcPpnfv3pX3MXmSJEmSWtCMGTNYc801GTJkCBHR7HBWKJnJSy+9xIwZMxg6dGjl/Ry2J0mSJLWg119/nfXWW8/EqQEigvXWW6/LvXomT5IkSVKLMnFqnKX5bE2eJEmSJKkC5zxJkiRJy4EhR/2+W483/fi9l9imV69ebLXVVrz55psMHTqUX//61/Tv37/L5zr33HOZPHkyP/vZz5Yi0tZhz5MkSZKkulZffXWmTp3KQw89xLrrrsvpp5/e7JCayuRJkiRJ0hKNGDGCmTNnAvDkk0+y1157sf322zNy5EgeffRRAH7729/ywQ9+kG233ZaPfexjPP/885WOPXbsWI444gh23nlnNtlkEy677LK36k488UR22GEHtt56a4499lgATjjhBE477TQAjjzySHbddVcAJk2axOc//3kWLlzI2LFj2XLLLdlqq6045ZRTuuUzMHmSJEmS1KmFCxcyadIk9t13XwDGjRvHT3/6U6ZMmcJJJ53EoYceCsCHP/xh7rrrLv70pz8xZswYTjjhhMrnmDVrFrfffju/+93vOOqoowCYOHEijz/+OPfccw9Tp05lypQp3HrrrYwaNYrbbrsNgMmTJzNv3jwWLFjA7bffzsiRI5k6dSozZ87koYce4sEHH+Sggw7qls/BOU+SJEmS6nrttdcYNmwY06dPZ/vtt2f33Xdn3rx53HHHHey///5vtZs/fz5Q3JvqM5/5DLNmzeKNN97o0j2U9ttvP1ZZZRU233zzt3qsJk6cyMSJE9l2220BmDdvHo8//jgHHHAAU6ZMYe7cufTp04ftttuOyZMnc9ttt3HaaacxcOBAnnrqKQ4//HD23ntv9thjj275PEyeJEmSpGXQ1YUcqizU0Cra5jzNmTOHffbZh9NPP52xY8fSv39/pk6dulj7ww8/nG984xvsu+++3HzzzYwfP77yufr06fPW88x86/Hoo4/m4IMPXqz9kCFDOOecc9h5553Zeuutuemmm3jyySfZbLPNiAjuv/9+rrvuOk4//XQuueQSzj777C6///YctidJkiSpU2uvvTannXYaJ510EquvvjpDhw7l0ksvBYoE5/777wdgzpw5DBo0CIDzzjtvmc+75557cvbZZzNv3jwAZs6cyQsvvADAqFGjOOmkkxg1ahQjR47kzDPPZNiwYUQEL774IosWLeLTn/40P/rRj7jvvvuWORaw50mSJElaLjS7x2rbbbdlm2224eKLL+bCCy/kkEMO4bjjjmPBggWMGTOGbbbZhvHjx7P//vszaNAgdtppJ55++ullOucee+zBtGnTGDFiBABrrLEGF1xwAQMGDGDkyJFMmDCBESNG0K9fP/r27cvIkSOBIsk66KCDWLRoEQA//vGPl+3Nl6KtS2xlMHz48Jw8eXKzw5AkSdIKpFHD9qZNm8Zmm222NCGponqfcURMyczh9do7bE+SJEmSKnDYniRJkqQeMWHChLfmSrXZf//9OeaYY5oUUdeYPEmSJEnqEcccc8xykyjV47A9SZIkSarA5EmSJEmSKjB5kiRJkqQKTJ4kSZIkqQIXjJAkSZKWB+PX7ubjzVlik169erHVVlu99frKK69kyJAhi7WbPn06++yzDw899FB3RthyTJ4kSZIk1bX66qszderUZofRMhy2J0mSJKmSefPmsdtuu7Hddtux1VZbcdVVVy3W5qmnnmLbbbfl3nvv5cknn2SvvfZi++23Z+TIkTz66KMdHnvs2LEcccQR7LzzzmyyySZcdtllb9WdeOKJ7LDDDmy99dYce+yxAJxwwgmcdtppABx55JHsuuuuAEyaNInPf/7zLFy4kLFjx7Lllluy1VZbccoppyzz+7fnSZIkSVJdr732GsOGDQNg6NChXHrppVxxxRWstdZavPjii+y0007su+++b7V/7LHHGDNmDOeccw7Dhg1jt91248wzz2TTTTfl7rvv5tBDD+XGG2/s8HyzZs3i9ttv59FHH2Xffffln/7pn5g4cSKPP/4499xzD5nJvvvuy6233sqoUaM4+eSTOeKII5g8eTLz589nwYIF3H777YwcOZKpU6cyc+bMt4YSvvLKK8v8eZg8SZIkSaqr/bC9BQsW8N3vfpdbb72VVVZZhZkzZ/L8888DMHv2bEaPHs1vfvMbtthiC+bNm8cdd9zB/vvv/9b+8+fP7/R8++23H6ussgqbb775W8edOHEiEydOZNtttwWK3q/HH3+cAw44gClTpjB37lz69OnDdtttx+TJk7nttts47bTTGDhwIE899RSHH344e++9N3vs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\n",
      "text/plain": [
       "<Figure size 1008x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.show()\n",
    "\n",
    "true = (df_true['month'])\n",
    "fake = (df_fake['month'])\n",
    "\n",
    "plt.figure(figsize = (14,6))\n",
    "plt.title(\"Distribution of Publication Date\", fontsize=20)\n",
    "plt.hist([true, fake], bins = 25)\n",
    "plt.legend([\"Real_news\", \"Fake_news\"])\n",
    "plt.ylabel(\"Number of News Released\", fontsize=16)\n",
    "plt.xlabel(\"Month - Date\",fontsize=16)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Fake news evenly distributed by month but the Real news mostly October to December "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA08AAAGNCAYAAADJgUqMAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAA+0UlEQVR4nO3deZhcZZmw8fshhARBCFsUkmCCHyphCxCQMCaDIssIQ5jRaFAHgmgcRHAbB5BRIpKBD1AGFPVDJywCYkAF3CDsiwiYYJBdtoAJkQSESBRCSJ7vj3Mayqa6czpdla7uvn/XVVdVve97znmqTlVST7/LicxEkiRJktS5tXo6AEmSJEnqDUyeJEmSJKkCkydJkiRJqsDkSZIkSZIqMHmSJEmSpApMniRJkiSpApMnSX1ORNwYET12HYaIOC8iMiJG1pSNLMvO66m4yjh69L1plIjYOiJ+GhF/Kt/X51sgpi6/t2XsN7Yrm1aW79nA8Lqlr3xuJKm7TJ4ktaTyx2PtbVlELI6IuyLi+xHxTxExoEnHnhcR85qx72arl7j1NeV5vxx4H/Bz4KvAKRW2a/+ZWhERz0TE9RHxkeZG3dp64+emLaGrub0SEc9FxIMRMTMiDouI9Rt0rJb444eknrd2TwcgSavw1fJ+ADAE2Bb4N+BwYHZEfCQz/9Bum0OAN6yxCF/vOIof8wt6MIaO9PR70wijgNHA9zJz6mps3/aZGgi8HTgIeHdE7JKZn29MiN3yLeAS4MmeDqRGK39uzgfmAQFsQPH5eC8wCfjviDg8M3/Zc+FJ6ktMniS1tMyc1r4sIt4EfJPix9G1ETE2MxfVbNOjPzozcyGwsCdj6EhPvzcNskV5/9TqbNz+MxURewHXAJ+NiLMyc163ouumzHwGeKYnY2ivxT8352XmjbUFETEY+AJwIvDTiNg7M2/uieAk9S0O25PU62Tm08Bk4EZgBPCl2vp68zOicGhE3FYO/3spIv4YEVdHxIfKNnuW270FeEu7IUHn1ewry2O8uRxCuKAcAjalrO90CFREvCMiLo+IP0fEXyPi1ojYp067Due+1BtGVMZ+aPn08ZrY53X23pTla0XEv0fEbyNiaRnXbyPiiIh43f8VNe/BphFxTkQsLIdW3hcRh9V73Z2JiF0i4scRsajczxMR8e2I2Lz9cYGbyqcn1LzGaV09ZpvMvA54kKLnYtfyOB2ew7bPSUfHjIhBEXFSRDxevpZHI+KEiFinSjyrOO/viIgZUQwtXVa+X7dExBHt2h0UERdGxB/Kc7k0IuZExNHtz2dv/tx0JDNfyszpwEnAOsCZ7eLYIiK+EhG/jmLe3MsR8VREXBwR27RrOw14vHx6aLt/F6a0a7tvRPwyiuGgbef+tIgY0qjXJqln2fMkqVfKzJURcRKwJ3BwRHwuMzub0D6dYjjd48BMYAmwOcWP5UnAjyiG/nwV+Gy5zf/UbD+33f42Bm4HlgI/AVYCT1cIfRTwG+Be4P+VMXwI+FVEfDgzf1RhHx35KsUQtB0pfiw+X5Y/X7/53/kB8GHgj8D3gQT+Bfg28C6g3pygIcCvgZeBy4DBwAeAGRGxMjPPrxJ0RBwA/JgiebkMeALYBTgCmBgR/1DTG/RVYCTFj/2bKBJoau5XV5T3jVgUYSbF5+oyYDkwEZgGjI2IA1fxOe04wIj9gUuBQcBVwA8pzsGOwH8C36lpfgrFZ/IOiuGjGwLvofhc7Eox9LVNr/zcVHQ68EVgTERsm5n3leUTgGOBGyg+e0uBrcs4Diw/c3eXbW8sY/4McDfFfLs2c9seRMRXKN7LP1PMxVsE7AD8B/C+iBiXmX9p4GuT1BMy05s3b95a7kbxIyxX0WYQxY/TBEbVlN/YflvgWWA+8IY6+9m03fN5wLxVxQZcAKxdp/68sn5kTdnImu1Oa9d+bPk6ngM2qCmfVrbfs84x2vZ33qqO3a6+3ntzcLnNXcD6NeXrAbPLug938B58HxhQUz4aeAW4v+J5Xp9iiNoKYHy7umPKY8xqV75nWT6tEZ8pivkxK8vbW1b1PnZ0/Lb3FvgDsFFN+WCKhDmBf6sT043tyl533oFNKRL+l4F/rBPT8HbP31qnzVoU84MSeGdv/ty0e79f9/1o1+6Wst1hNWVDgTfWabsjRSL1qyrft5r6d5f1twFD2tVNKevO6Mrn1Zs3b615c9iepF4rM5dRJEUAm1XYZDnFj/T2+1md+SUvA/+Rma90cbslFPMwao8/G7iI4q/b/7IasXTXx8r7YzNzaU1cf6VIYAA+Xme7vwGfz8wVNdvcT9GrsE1EvLHCsScCmwA/ysxb2tV9nSKR3TsitqzyQqooh8VNi4jpEXEZRS9OAP+TmU804BBfy8zn2p5k5ksUvZ7w2nvdVYdSLIbwncy8qX1lZs5v9/zROm1W8trwtX1XM45aPfm56Yq2hVte/TciMxdl5gvtG2bR23Q9xQIiA7twjKPL+09k5vPt9nkeRQ9Vv17RUeorHLYnqberOtzqIuAo4L6IuJRiyNdvMnPJah53XtYsUtEFd9X70UbxV/RDgZ0oegfWpJ0pel1urFN3E0XCuVOduoez/jCkP5b3Q4B6r7X9saH4wfp3MvOViLiZ4q/+O9G41edOaDsExdC0W4D/zcwLG7T/1yU35TFeof77WMXu5f2vqjSOiE0ohqu9D9iKojeo1rDVjKNWT35uuqLuvxHlMMh/p+j53ZTX/ybalOoLv4yj+OPMpIiYVKd+HWCziNgkM5+tUy+plzB5ktRrRbGi1sbl08WraP454FGKv5YfW95eiYhfAl/IzEe6ePg/dbF9m47mRbXtb8PV3G93bAj8OTNfbl9RJjDPUAxzau/5DvbX1htX5Tpcba+3ox+pbeVDKuyrksyMVbfqlted48xcERHPUv99rGJIeb/K5e/LxQl+SzG/7k6K4aV/pjgvQyjm7gxazThq9eTnpivaVmd89d+IiDiaohfuOYqVFp+k6BFLXpv/1ZX3aBOK31QnrKLd+rzWWy6pFzJ5ktSbvYvi37GncxXLS5dDhM4EzoyIoeW2kykWi9i2nEy+rAvHXt2FBd7UQfmby/vanrCV5X29f6uHrObx61kCbBwRAzNzeW1FRKxN8Rf4Zk10b3u9b+6gfvN27daU7rz3b6JdL1kUF/bdhNV/H58v74cB96yi7ccpEqev5uuXZR9HkTw1Qk9+biophwDuUj69oyxbm2Jhhz8BO2dxaYHabcatxqGWAGtl5sarbCmpV3POk6ReqVwG+fjy6cVd2bac7/CTzPwgxXCxtwLb1TRZQeP/+t1m5w7mdOxZ3v+upqxt3syIOu3HdrD/tnkkXYn/dxT/H0yoUzeh3NddXdhfV7S93j3bV5Q/ct9VPm3W8TuyOu99m3+sUzaeIhH7XZ26Km4v7/+pQtv/U97/uE5dvdig931uqvoisC7wu8x8oCzblCIBvq1O4rQ+rw0lrbWq9+d2YKOI2LbbEUtqaSZPknqdsufoEoof3E8C/72K9oMiYq+IiHblA3lt2N/faqqepZifsG7Dgn7NhsBX2sUxlmIy+RLgpzVVd5b3h5WJRFv7Ee33UaNtSFBXFliYUd6fHBFvqDnOGyiWvAb43y7srysupxhSdnBE7N6u7rMU83WuzTV/kda29/4TtYURsT2r7rn5ckRsVLPNYODk8um5qxnP+RS9OEdExOuSlYgYXvN0Xnm/Z7s2O/HawhXt9bbPTaciYnBEfIniDywv89qCDlAsIf43YJcyWWrbZiBF7/SmdXb5HEVvc0fvzxnl/fciYov2lRGxXp3Pt6ReyGF7klpavHYh0rUo/lq8LUVvxDoUP3A/UmG1vHWBa4F5EXEHxXWEBgN7A9sAV9b8VRrgOopr4VxVLliwDLg7M3/WgJd0M/DxiHgnxepibdd5Wgv4ZO1E+sy8ozz+BODOiLieYkjYPwNXU79X5DqKv7Z/r1xJbinwfGZ+q6OAMvPiiJgIfJBiQY3LeW3uxyhgZmZe1K1X3fGxl0bExyiuX3RTuZjHkxRDrfahGFr1yWYcexWuAB6mSOqGUwz52pJidcArKN6rjjxA8T7WXufprcAvKK6L1GWZ+UxEfJjiukg3RMSvgN9TrMC3A8VnYVTZ/AKKz8D/RMS7y9exNXAAxTXJPlTnEL3qc9POlHjtgsLrU7zXEyj+MLIQ+Fhm3loT98qIOIti3uM9EXEFxb8n7y63uaF8TM02S8t/O8ZHxEUUy9GvoPi34/eZeV1EHEuRJD9czqV8vIznLRQ9frcC+zXh9Utak3p6rXRv3rx5q3fjtevBtN2WUVwPaA7wPYofIWt1sO2N1FyTBhhIcRHRX1H8MH+JYvL47RSrba3Tbvv1KC44Op9iEvvfXd+FOtfmabf9eXR8nafzKBK2Kyj+mv03iiRq3w72NaR8vYvK9+BeYCqdXHcG+DzFD/hlZZt5Hb03NeVrAZ+iuD7P38rbHODIeu9zZ+9Bvddf4XzvStHrtpiip+DJ8hxsUaftnjTwOk+dtB9BcfHkPwMvUizC8K8dHZ/Xrjs0CDiJ4sfzMuAxioUEBlV5H+n8+l7bUiRHC8r36WmKle2mtms3Griy/Nz8tTyXH+9Ln5ua97vt9grF3LAHy/M2BVivg23XLl/v/eW5/RNFYvuWjuKgGA75M4peupVlmynt2ryL4iLJT5XnZzHFMuXfAMZ25fPqzZu31rxF5urOeZYkSZKk/sM5T5IkSZJUgcmTJEmSJFVg8iRJkiRJFZg8SZIkSVIFJk+SJEmSVEG/us7TpptumiNHjuzpMCRJkiS1qDlz5jyTmZvVq+tXydPIkSOZPXt2T4chSZIkqUVFxBMd1TlsT5IkSZIqMHmSJEmSpApMniRJkiSpgn4150mSJEnqLZYvX878+fN56aWXejqUPmnw4MEMHz6cgQMHVt7G5EmSJElqQfPnz+eNb3wjI0eOJCJ6Opw+JTN59tlnmT9/PqNGjaq8ncP2JEmSpBb00ksvsckmm5g4NUFEsMkmm3S5V8/kSZIkSWpRJk7NszrvrcmTJEmSJFXgnCdJkiSpFxh57C8aur95p+y/yjYDBgxg++2355VXXmHUqFH84Ac/YMiQIV0+1nnnncfs2bP51re+tRqRtg57niRJkiTVte666zJ37lzuvfdeNt54Y84+++yeDqlHmTxJkiRJWqVx48axYMECAB599FH2228/dtllF8aPH8+DDz4IwM9+9jPe+c53stNOO/He976Xp59+utK+p0yZwtFHH80ee+zBVlttxWWXXfZq3Wmnncauu+7KDjvswAknnADAqaeeyllnnQXA5z73Od7znvcAcN111/HRj36UFStWMGXKFLbbbju23357zjjjjIa8ByZPkiRJkjq1YsUKrrvuOg488EAApk6dyje/+U3mzJnD6aefzqc+9SkA3vWud3H77bfzu9/9jsmTJ3PqqadWPsbChQu59dZb+fnPf86xxx4LwKxZs3j44Ye58847mTt3LnPmzOHmm29mwoQJ3HLLLQDMnj2bpUuXsnz5cm699VbGjx/P3LlzWbBgAffeey/33HMPhx12WEPeB+c8SZIkSarrxRdfZMyYMcybN49ddtmFvffem6VLl3LbbbcxadKkV9stW7YMKK5N9aEPfYiFCxfy8ssvd+kaSgcddBBrrbUWo0ePfrXHatasWcyaNYuddtoJgKVLl/Lwww9zyCGHMGfOHF544QUGDRrEzjvvzOzZs7nllls466yz2HzzzXnsscc46qij2H///dlnn30a8n6YPEmS6pu2YRfaLmleHJKkHtM252nJkiUccMABnH322UyZMoUhQ4Ywd+7c17U/6qij+PznP8+BBx7IjTfeyLRp0yofa9CgQa8+zsxX74877jg++clPvq79yJEjOffcc9ljjz3YYYcduOGGG3j00UfZZpttiAjuvvturr76as4++2xmzpzJjBkzuvz621ujw/YiYkZELIqIe9uVHxURD0XEfRFxak35cRHxSFm3b035LhFxT1l3VrgAvtSxaRtWv0mSJNWx4YYbctZZZ3H66aez7rrrMmrUKC699FKgSHDuvvtuAJYsWcKwYcMAOP/887t93H333ZcZM2awdOlSABYsWMCiRYsAmDBhAqeffjoTJkxg/PjxfPe732XMmDFEBM888wwrV67k/e9/P1/72te46667uh0LrPmep/OAbwEXtBVExLuBicAOmbksIoaW5aOBycC2wBbAtRHxtsxcAXwHmArcDvwS2A/41Rp8HZIkSdIaVWVp8Wbaaaed2HHHHbnkkku46KKLOOKIIzjppJNYvnw5kydPZscdd2TatGlMmjSJYcOGsfvuu/P4449365j77LMPDzzwAOPGjQNg/fXX58ILL2To0KGMHz+e6dOnM27cONZbbz0GDx7M+PHjgSLJOuyww1i5ciUAJ598cvdefCnausTWlIgYCfw8M7crn88EzsnMa9u1Ow4gM08un18NTAPmATdk5jvK8oOBPTPz9X157YwdOzZnz57dsNci9QoOvdLq8rMjST3qgQceYJtttunpMPq0eu9xRMzJzLH12rfCantvA8ZHxB0RcVNE7FqWDwP+WNNuflk2rHzcvryuiJgaEbMjYvbixYsbHLokSZKk/qIVFoxYG9gI2B3YFZgZEVsB9eYxZSfldWXmOcA5UPQ8dTtaSZIkSatl+vTpr86VajNp0iSOP/74Hoqoa1oheZoP/CSL8YN3RsRKYNOyfERNu+HAU2X58DrlkiRJklrY8ccf32sSpXpaYdje5cB7ACLibcA6wDPAlcDkiBgUEaOArYE7M3Mh8EJE7F6usncIcEWPRC5JkiSp31ijPU8R8UNgT2DTiJgPnADMAGaUy5e/DBxa9kLdVy4mcT/wCnBkudIewBEUK/etS7HKnivtSZIkSWqqNZo8ZebBHVR9tIP204HpdcpnA9s1MDRJkiRJ6lQrDNuTJEmSpJbXCgtGSJLWkJHH/qJy23mDmxiIJKnrunL9vUr7W/U1+gYMGMD222//6vPLL7+ckSNHvq7dvHnzOOCAA7j33nsbGWHLMXmSJEmSVNe6667L3LlzezqMluGwPUmSJEmVLF26lL322oudd96Z7bffniuueP2i14899hg77bQTv/3tb3n00UfZb7/92GWXXRg/fjwPPvhgh/ueMmUKRx99NHvssQdbbbUVl1122at1p512Grvuuis77LADJ5xwAgCnnnoqZ511FgCf+9zneM973gPAddddx0c/+lFWrFjBlClT2G677dh+++0544wzuv367XmSJEmSVNeLL77ImDFjABg1ahSXXnopP/3pT9lggw145pln2H333TnwwANfbf/QQw8xefJkzj33XMaMGcNee+3Fd7/7XbbeemvuuOMOPvWpT3H99dd3eLyFCxdy66238uCDD3LggQfygQ98gFmzZvHwww9z5513kpkceOCB3HzzzUyYMIGvf/3rHH300cyePZtly5axfPlybr31VsaPH8/cuXNZsGDBq0MJn3/++W6/HyZPUi/TlTkr4LwVSZK0+toP21u+fDlf+tKXuPnmm1lrrbVYsGABTz/9NACLFy9m4sSJ/PjHP2bbbbdl6dKl3HbbbUyaNOnV7ZctW9bp8Q466CDWWmstRo8e/ep+Z82axaxZs9hpp52Aovfr4Ycf5pBDDmHOnDm88MILDBo0iJ133pnZs2dzyy23cNZZZ7H55pvz2GOPcdRRR7H//vuzzz77dPv9MHmSJEmSVMlFF13E4sWLmTNnDgMHDmTkyJG89NJLAGy44YaMGDGCX//612y77basXLmSIUOGdGnO1KBBg159XFz6tbg/7rjj+OQnP/m69iNHjuTcc89ljz32YIcdduCGG27g0UcfZZtttiEiuPvuu7n66qs5++yzmTlzJjNmzOjW63fOkyRJkqRKlixZwtChQxk4cCA33HADTzzxxKt166yzDpdffjkXXHABF198MRtssMGrQ/2gSILuvvvuLh9z3333ZcaMGSxduhSABQsWsGjRIgAmTJjA6aefzoQJExg/fjzf/e53GTNmDBHBM888w8qVK3n/+9/P1772Ne66665uv357niRJkqTeoMLS4s32kY98hH/+539m7NixjBkzhne84x1/V7/eeuvx85//nL333pv11luPiy66iCOOOIKTTjqJ5cuXM3nyZHbccccuHXOfffbhgQceYNy4cQCsv/76XHjhhQwdOpTx48czffp0xo0bx3rrrcfgwYMZP348UCRZhx12GCtXrgTg5JNP7vbrj7busP5g7NixOXv27J4OY/V0ZV3/FvhiqXm6Pufpw9Ub+9np87p2nSc/O1pNXb0WjZ8fqa4HHniAbbbZpqfD6NPqvccRMSczx9Zrb8+TJElaJS+wLEkmT5IkSZLW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\n",
      "text/plain": [
       "<Figure size 1008x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.show()\n",
    "\n",
    "true = (df_true['day'])\n",
    "fake = (df_fake['day'])\n",
    "\n",
    "plt.figure(figsize = (14,6))\n",
    "plt.title(\"Distribution of Publication Date\", fontsize=20)\n",
    "plt.hist([true, fake], bins = 25)\n",
    "plt.legend([\"Real_news\", \"Fake_news\"])\n",
    "plt.ylabel(\"Number of News Released\", fontsize=16)\n",
    "plt.xlabel(\"Date\",fontsize=16)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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xeTJkzn11FOBJsG58sorAbj33nvZbLPNADj++OOX+by77bYbxxxzDAsWLADg1ltv5Y477gBg+vTpHHnkkUyfPp1p06bxpS99iSlTppCEu+66i0WLFvHa176Wj33sY1x++eXLHAvY8yRJkiStEMZ71MN2223HC17wAk4++WROPPFEDjroID7+8Y/z8MMPM2PGDF7wghcwc+ZM9tlnHzbbbDN23HFHbrnllmU656677sq1117LTjvtBMA666zDN77xDTbZZBOmTZvGrFmz2GmnnVh77bWZMGEC06ZNA5ok64ADDmDRokUAfOITn1i2i29loEtsVTB16tSaPXv2eIchqQ85bE+S1G+uvfZattxyy/EOY6U21HucZE5VTR2qvcP2JEmSJKkDh+1JkiRJWi5mzZr16FypAfvssw8f/OAHxymikTF5kiStVEYyBNPhl5K0fH3wgx9cYRKloThsT5IkSZI6MHmSJEmSpA5MniRJkiSpg3FJnpKsnuQXSb7Xvn5aknOS3NA+btDT9rAkNya5PsluPeU7JLmqrTsqScbjWiRJkiStGsZrwYh3AdcC67avDwXOrapPJjm0ff3+JFsBM4CtgWcCP0ry11W1EPgicCBwCXAmsDvwg+V7GZIkSdJyMnO9UT7evUtssvrqq7Pttts++vo73/kOkyZNekK7uXPn8upXv5qrr756NCPsO8s9eUoyEdgDmAW8ty3eC9i5fX48cAHw/rb85Kp6ELglyY3Ai5LMBdatqp+1xzwB2BuTJ0mSJGnUrLXWWlxxxRXjHUbfGI9he/8F/AewqKfs6VU1H6B93KQt3wz4XU+7eW3ZZu3zweWSJEmSxsiCBQvYZZdd2H777dl22205/fTTn9Dm5ptvZrvttuPnP/85N910E7vvvjs77LAD06ZN47rrrhv22Pvvvz+HHHIIL37xi3nOc57Daaed9mjdEUccwQtf+EKe//znc/jhhwPwqU99iqOOOgqA97znPbziFa8A4Nxzz+UNb3gDCxcuZP/992ebbbZh22235bOf/ewyX/9y7XlK8mrgjqqak2TnLrsMUVaLKR/qnAfSDO/jWc96VrdAJUmSJHH//fczZcoUACZPnsypp57Kt7/9bdZdd13uuusudtxxR/bcc89H219//fXMmDGDY489lilTprDLLrvwpS99iS222IJLL72Ut7/97Zx33nnDnm/+/PlcfPHFXHfddey555784z/+I2effTY33HADl112GVXFnnvuyYUXXsj06dP59Kc/zSGHHMLs2bN58MEHefjhh7n44ouZNm0aV1xxBbfeeuujQwnvueeeZX4/lvewvZcAeyZ5FTABWDfJN4Dbk2xaVfOTbArc0bafB2zes/9E4La2fOIQ5U9QVV8GvgwwderUIRMsSZIkSU80eNjeww8/zAc+8AEuvPBCVlttNW699VZuv/12AO6880722msvvvnNb7L11luzYMECfvrTn7LPPvs8uv+DDz642PPtvfferLbaamy11VaPHvfss8/m7LPPZrvttgOa3q8bbriBfffdlzlz5nDfffex5pprsv322zN79mwuuugijjrqKDbddFNuvvlm3vnOd7LHHnuw6667LvP7sVyTp6o6DDgMoO15+reqekOSI4D9gE+2jwP9f2cAJyX5DM2CEVsAl1XVwiT3JdkRuBTYF/j88rwWSZIkaVVz4okncueddzJnzhzWWGMNJk2axAMPPADAeuutx+abb85PfvITtt56axYtWsT6668/ojlTa6655qPPq+rRx8MOO4y3ve1tT2g/adIkjj32WF784hfz/Oc/n/PPP5+bbrqJLbfckiRceeWVnHXWWRx99NGccsopHHPMMct0/f1yn6dPAq9McgPwyvY1VXUNcArwK+CHwMHtSnsABwFfBW4EbsLFIiRJkqQxde+997LJJpuwxhprcP755/Ob3/zm0bonP/nJfOc73+GEE07gpJNOYt111310qB80SdCVV1454nPutttuHHPMMSxYsACAW2+9lTvuaAaqTZ8+nSOPPJLp06czbdo0vvSlLzFlyhSScNddd7Fo0SJe+9rX8rGPfYzLL798ma9/vJYqp6ouoFlVj6q6G9hlmHazaFbmG1w+G9hm7CKUJEmS+kiHpcXH2r/8y7/wmte8hqlTpzJlyhSe97znPa5+7bXX5nvf+x6vfOUrWXvttTnxxBM56KCD+PjHP87DDz/MjBkzeMELXjCic+66665ce+217LTTTgCss846fOMb32CTTTZh2rRpzJo1i5122om1116bCRMmMG3aNKBJsg444AAWLWrWqfvEJz6xzNefge6wVcHUqVNr9uzZ4x2GpD406dDvj6j93E/uMUaRaFmN5LP0c5TUz6699lq23HLL8Q5jpTbUe5xkTlVN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\n",
      "text/plain": [
       "<Figure size 1008x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.show()\n",
    "\n",
    "true = (df_true['week_day'])\n",
    "fake = (df_fake['week_day'])\n",
    "\n",
    "plt.figure(figsize = (14,6))\n",
    "plt.title(\"Distribution of Publication Date\", fontsize=20)\n",
    "plt.hist([true, fake], bins = 25)\n",
    "plt.legend([\"Real_news\", \"Fake_news\"])\n",
    "plt.ylabel(\"Number of News Released\", fontsize=16)\n",
    "plt.xlabel(\"Weekdays - Date\",fontsize=16)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "More Real news realized during weekday"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([6, 4, 5, 3, 0, 2, 1])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_true['week_day'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_true['target'] = 1\n",
    "df_fake['target'] = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "combined_df = [df_true, df_fake]\n",
    "df = pd.concat(combined_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Resetting the index since combining 2 df creates duplicate indexes\n",
    "df.reset_index(drop=True, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAzcAAAF0CAYAAAAegscxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAADlxUlEQVR4nOz9V8wtWZbnh/12+OPNZ6+/N72tykpXvpvdIwmESBF64IsAGZIiBhIgiaQMMW8cDShDCTIDPogaDDmkqBEEkoAggsTMdA97urxLV5mVlT6vd589/pywWw8R50TEOedm3pudNyvn0/oBja4vMnacFWvt9d977dgRV2mtEQRBEARBEARB+Kcd4w9tgCAIgiAIgiAIwpeBFDeCIAiCIAiCIJwIpLgRBEEQBEEQBOFEIMWNIAiCIAiCIAgnAiluBEEQBEEQBEE4EUhxIwiCIAiCIAjCicD6QxtQZHNzU1+8ePEPbYYgCIIgCIIgCF9jXn/99QOt9dby8a9VcXPx4kVee+21P7QZgiAIgiAIgiB8jVFKXV13XLalCYIgCIIgCIJwIpDiRhAEQRAEQRCEE4EUN4IgCIIgCIIgnAikuBEEQRAEQRAE4UQgxY0gCIIgCIIgCCcCKW4EQRAEQRAEQTgRSHEjCIIgCIIgCMKJQIobQRAEQRAEQRBOBFLcCIIgCIIgCIJwIrAe9g8opdrA3wWeAzTwr2itf/Gwf/fLwvd9+gEESULFNtmoOoxmAaMwIdGaum3RrNgcT0PGQYRtKFqeiWfb7I99/CjBMw026+7a6/enAeMgxlCKqmvRdC0Oxz7TKMExDZqWxjBNen5CECdUHZNuxWEwS9tpoOFYNDybWRinNpgGddfCn80YxQZ+nOBZBps1lyjRjPyQWKftHMugPwkYhTGmoWjaFlXPojcNmIQxnmXSrTpMg4BhkBDEmqqdHgvjmKEfo4C6a2GbBkfjgEkU45gGLRssy+JoGuHHCTXbpFN1GPgBYz9Ba03NsWhVbHqZHyxD0XBMqq7NwdhnFuW2B2HM8SwkSjQNx6RZcRj5IQM/wlCKlmtScWyOJqntjmnQcdP6/XiWECQJVcukW3PoZ/enM9ubrk0v84NjKOqeSdXObahYBhs1l9E0ZBTFxImmZpu0qw69WcDYT/1Xty3qXh5D1zRoOSq1IUgIY03NNuhUXYazgFEQA1B3TBqew/HEZxwmOKai7RjEcbyI4cIGP2IURCSJpu6aND2H4+yeTUNRs0waFZvDic80THAtg62ayyQMGc1igkRTsy06VZuBHzLyIxSKqm3QqqTXGocxjmHQcrJ+GmiCOKFimWzUXYYzn1GQoDVUHYN2xeV47DOOYmzDoOFqqk6Fg9EsjaFtsFnzGE6nTCJFlGhqlkG75tIf+4yjBENB1TJoVt3Uf1kMmzYopVIbkoSqZdCteQymU8ZBKio1V9HyPI7GPpPMhroVU6vU2B/5+FHalzfrLqPpjFGoiTXUbUWr6tHL/G4qqDuKuudxMPKZRTGuZbJVdxlPJ4wigzBJqFkmnZpLfzJjHGoUUHOgWaksbHAMg7ZrkCQJg5DUf7bJRs1l4EdM/JBEQ80xaFVcepkfLENRtTSNSu4/1zLYqntMJhOGcWaDbdKpuvQmPpMwQSmoWwaNqsvhyGcaxbimQTPrf8sxHM18hlkM63bq97T/ZTG0NNVKhf3RLNUxy2CznsUwhEhDzVK0a14phnXXoO7mMXRNg4YNhmHQC1IdqzkmnYrLYDpjHOgsBxSNilfqR3XXwJjnQBQv/DeezBhGaQznedifpHE1VRrXesXjcDRL83AeQ99nFGjCJKFum7SrhRgqqBrQqlc4Gs+YhAmOZdCyFVrrRQyrtkm35jKc+Iyi1H81y6BVK8ewaWkqhRjO/TcNfQYzvTYHijE8GvsLHSvlQJxQtdMcWOiYhrpn0nQdehM/0zFjoWPzGFYsg426V8qBmq1oVz16Wd6bCuqmol7z8hhaJnUzISFhFJmlHBiOZ4yiLIaWolHLY5jmQESSWAxDUh3LYjjyfUZ+QqJZ6FhvPGMcaSwFVZv7zoHBxGeU5UDDNqhX3EXsnYIGr+jYxGccaRKtqdoG7eUcsBOqXpX94SwdRxc65jOJ1sfws3TMMKDnc28dy/SopGOOoua6qzo2mzEK5jpm0Kq69LK+bCqoG4p6fZ2OTRlFinAxHt5Lx2ZMoiSLYUKSGGt0zGeSxXBdDix0bDxjFqbj4Vbjs3XMUIqapT5Xx2q2Qafm0Z/MmET63jpmJlSr1fvSsUE2BzAU1E2Dem2djkX0fIugkAODrN+uy4H5WGRgrOrYeMYwLuvYYDJjFCaYStG0oVKprOjYH4Ll+djXnYde3AB/G/iHWut/USnlANWv4De/FAaTkNvjgLdvD4m1pmIbvHquw63+mI8OZwBs1xye323y6xs9hn6EAp7ZrtOp2Pzqeo8w0TimwctnW5xvl299f+Tz1u0+h5MQgIudKo90K/z86jGzTBxeONWkYkX87Fo/mwiZvHq2zYf7I24OfQBONVye3Wnwy2vHjII0MX94vskkNnjz1jFRonEtg1fOthn7AW/dHqGBjarNC6davHGrz/E0RAGPbFS52PH46eUefpza8OKZFlEc89btYToQOSavnGvzwd6IW5kNl9oVLnSr/Pp6L51kK3jhdAtDhbxxa0CcaDzL4NvnOlzrTbh8PAVgs+rwzVNNXrvZoz9L/ffkVp2tmsOvrh8TxBrbVLx8pk01CfjLG2M00HQtXjnb5rd3BhyMAwAutD0e7db5+bUjZlGCmfnPAN641SfWULVNXj3X5tOjMdd6aQx36g7Pbjf4zc0+Qz/CUPDUVp3uUgxfOdvmeBry3t4QDbQ9mxfPtHjrVp+jaRrDS90qj3Qq/PTqMf48hqebGFrz2q1BIYYd3t8fcrsQw2e2GvzyxnFW7MKz2w1aFYtfXjssxfBoMuP3exMAulWbb51q8frNHr3Mf49v1jjV8PjFtWOCOMHOYhhHEa9nsW9k/nv3zoC7mf/OtTwe26zxq2t5DJ8/1WTTs/jR5eM0ByyD717o8PFh7r+tLAdeu9Fj4M9jWONcS/GjK0eEscYxFS+daaO05hfXe2ig5Vm8fKbNW7cHHE5SGy62KzzW1fz02vEihn9yqcv+JOCdO6n/FjE8mHBtkNqwW3d5Zgd+fb23yIGntxtshhN+drWX+s80eOVcm72hz0eHaT/qVGxePK3KOdCtcr6t+fm13iKGL55u0bRjfnQlz4Fvn2vz7t0Rd0ZpDE83PJ7aVvzqWo9xNkA+t9Nko2Lzk6tHRFkOfO9Ch0+PJlzJcmCj6vDNUw1ev9lf5MDjGzXOtxU/vpLH8KWzLXQU8utbeQ68fLbN7+4M2CvE8IlNzc+vHTPNBshvn2sxjZIVHbvRH/PJZ+jYU1t1Tsfw48vHJR1TScLPr/ezHLB48Qz89vagoGMVHumkNsx17IcXuhxMZ7x7d7jIgVfOtrmyP+JKIQee3i7H8IfnG0xic0XHjscBv99P+3K3YvOt0y1evzWgl8Xw0Y0qFzuan1xJdWyeA56K+Mn1EUm2uPPKuRbv3h1xN4vh2ZbHE1rxy4KOff9Cm1Go+e3tXMdePdfhZn/CJ0efpWM1tgL45fVjwoKOjfyA390tx/Dtgo492vU4E2l+ff24pGMKeHNZxw7HXOvnOvbcToNfX+8zDFId+6Pzde4mFm/c7Jd0bOxH/PbOII1hlgPLOnYpgZ9dy3XsW6dbKBJeu9krjUXv748WOna64aY5cL2gYzsNtqrw4yt5Dnw/y4H5OJDqWJPXb/YXOvbYRo1TTcUvCzr20pkWkyDinbtFHWvxuzvDUg48vqn55ZKOdVyLH1/5Ijpm8OMrR5n/Uh3zo4Q3b/UXOvbSmRa/vT0s69iG5qeFsfybp5pULMXPr/VKOnb5YMLVgo49uwO/WtKxnVrMj6/kOvbquTZ3l3TsW6dbvHlrUNKxi1rz06v5WP5HF9vcHUe8t1cey9/7HB37xm4Tz9L85ma/kANt9kdT3tu/t449sVljp6745fWjdCzPdMwPQt66c28de2LT41SWA9Mo1bFvnGqw6Zj86OrxIge+c77NRwdjrvdzHXtut8FvbvRLOnYmmZZ07IcXO1zr+Xyc+a/tWbx0Bt68PeAo07FLnQqXkrKOvXCqiaHgtZuHixz49rkO7xfmQqcaLs9swy+v9xY58NLpJihWdOxwPOO9/Wwsr9i8cLrFGwUde3q7TseH39zo5WP56Ranaiae5/FV4Ps+dyYxr93slcby3aqJ6359i5yHui1NKdUE/gj49wG01oHWuvcwf/PLZBTFvHlrQKzTinwaJrx+o8fFTn1xzt444OZgytlmGmQNvLs3YuDHhEnaLogTfnO9x/7YX7QLgoArvcliQgBw5XhCfxYRRAkAUaJ5/WYfw7DILsU4iHnr1gDDUIt2t4c+d4Y+F9tpZ080GKbN6zdTMQTwo4Tf3OixUfPILkWcaD4+HHOcDWga+ORwwshP8OPchtdu9PCs3IZREPPOnSFPb+d+aFVs3rzVZxKmTyJind73azdSMQSYRQmv3ehhqNz2g0nA9d4UO7sfDby/P0r9EKftwljzmxs9tJPbHiWaa/3pYkIAcLU3Y2/sE2S2x5n/ZnFCdikmYcwbN/t0K86inVKK3+0NGfrRwn+/3xvRX47hjWOarrWwoTcL+fhwRM0xF9e6fDRh4MdExRje6GOZZimGv73d5/GNWimGexMfK3NNouGdu0OihFIMX7vRY6deWbQ7moRcOZ6wU3MW/vvwII3p3A9hFsOa5yxsH/oRv7sz4NFuXnBf78/YGwWL2Mca3ro1wE9Y5ECYJBxPo8WEAGB/HHCjP13YmcZwzDh7UpX6L41hxcn9ZxuKa73pYkIAcKU35diPQOUx9ON0YpkUYvjmrT5n27kf7ox8bg/8xe8lGt69O8SPCv7L8hDFwobjacgnh2MSndv+ydGEkR8TFmL42s0ekXIWNqS/GSwmBAC3hjPuFvyXaHj7zoBI64UNQZTQn0WLwgbgcBJwtTdd5IkGPjwcMwrjUgx/c6NPrZLnwMCP+P3dIZe6uR+u92ccTyPQ8xhqUGpFx9640edcK+9/cx0zs/6ngff2R0wjvZQDPTzHLuRAxEcHYx4r9KMrx1P6flnHIq15586wrGO3Bzy63Vi0uz302RsFdDxz4T/DdHjtRm8lBzbqeV8+moZ8ejQhKfjv48MJw4KOpf7rYVjuwgal4M7QXxQ2ADf6M46mIWamR7EGpUzeuFnWsddv9OgUNORgEnCtN6VmGQsb3t8f059Fiz4517Gaa5di+N7ekG+fbi6u1a64vH6zxywq65i/TsequQ13RwG3hj47dXvhP2W6/OZGbyWGnWohhtN76VhUzoEbvRUde/v2oKTnt4Y+d4azRewTDe/cGRIkeQ4kUcLAjxeFDcx1bErLtRb+++hwTG9Jx35zo0ekVUnH3r07RBVsuN7P8jAq61isl3UsXNGxm4Mpj3QqpRiOgqTgv9SGumsubOjPIj7YH5OrSqpjvVlEQu6/N272MQ1zRccuFsaBOyOfO6MAhVr47927Q/y4rGO/XqNjnx6N2ajk/vvkaMIoTIgKY7kfs1hggHQsf/v2kI2qXYjhjDvDso69dXvAOEyWxvI+u40871Mdm5XGgQ8OxvRnYT6WZzrWXKNjp5v5RPlMs8brN3tMo1zH3rw1wFdqkQNRrDmahIvCBuY6NiPMbJ/r2GRJx8ZBvCgMIdWxDw/GfOdcnoeX1+jY6zf7WIax8J9ONAfjYFHYQKpjd8cBpwp5aFvmWh3bqucFytE05PLRhMc6+Vyy6dqLwmbhv5s9Bvm08aEzCNPianks/ypt+CI87HduHgH2gb+nlHpTKfV3lVK1z2v0dWESRCvHRkE+4Z1zdxRwtlUpHYuSpPR3mGim2cQfYJYo9kYByxxPQ9qVXGg0LAqGxTmzkIZrl47dHfk8vpkXG5MgZslM/ChZDJgAnarDXmFgn9OfhbS9fKBLNAtxmnMwDkoDSsU26c/K/oqTotynjLMtDkXujHx2G+VViCBOH+/PiRK9EDpIVxvX2u5HVO3y9eNyKBj4EV7hnE7FZn9NLOIlBwaxXkyC5+yNAraXHhP3piEbtXzSoWExUMw5moZYpiod2xsFXOiUn+75YbndLErW9D+f3WZl6bx0i9/iXjSl2EM6mFec8sPb3jSk7pT9V+x/mzW3VIwUbW975T45Xuq3UaJL1zrV9EoTyzlHk5AnN/NJ7ziIV87pz6IV/+1PAlpe+X5mUbltuoJZlr27Y79U7ELaj2oF3yQapgU7dhvu2v53OAlouGUbivZ3q85idbzI3igo5T3AyI+pFQ7FS/4D2Bv71Jxyu/2xzyPdXAtmS30IYBhEK7l5dxRwqlHuy5Ml34exZrrk07ujgLq72o+K97Muhr1piGY5n3ye3M4nGPOtt0VmUbKYJBTbdZb815+FPLuZDzeJLvflUw2Xu2vyfm8UlIq1dePAOIyxzHI/2hv7nFvK3yBOKPbSKNErerQ/DvALt2Obxlp/LevRwI+oLGnd3sjnUsGGabg6DgRxspgs5e1Wdaw/i2gU8knDomCYczgNaS3l/eEkpLmUh8V+9Nh2jaPpqt/vjnxOtz5fx5bZGwUrse9NQ+pu2Tfj+9Cxu8OAneUcWKNj4ZIhe2O/VOxC6odzzTwW68by/iwqjXOQ6XmjfK3JUg6v07G9UcBOo+y/3jTkYicfW5evk9oZ0Fry39F0VceW+98kjFfycH9NHs6WxvI40WvGIp+Wl99zovViy3bpNwvHtuo2B2tiuL9GS4vtWp61WMgssjcKiOJyMHrTkFZlKQcKubPbdNeOYXvDso75UbJWx5Z9ujf26VTz/pdovZKryzr2sFkX53Q+9tXZ8EV42MWNBbwI/N+01t8CxsDfKJ6glPrrSqnXlFKv7e/vP2RzHgxvaeAAqNgG1pLXulWbvcGkdMxcUixTKTwzv55lpo8hl2l5FgO/PPnxln6w7pgrnXujanNrkK+ErbPdNhROYUI4mEUrQgRQd22Gs/z6CrCXJpJtz0YV+vt8H30Rc03vcq10n23ZdofDcVkgbFOVBmVDlf0w9KO1/ms4ZqkIWmdH1TYXKzvza63zw3I7y1AsjSd0Kja9pclq07M4npVF1126WNO1WHID3arNrUHZD45V9rtjqsVTrmK740m5nWsaJUFSgLdUVLYr9mJVqmjX8oS2OIE6noYrRQxAp2qvDBiVpX67HMODUUC3unqtdsXi08Nh4fdXO1LdMVcKzY5nMVyaiLpLNliGWm1XcVZyruFajAvXUpRz6nAclFY7F7Z71srEtGh/bxYsVqeLdCur/qvaJuOCWan/yjHsVByCuPx7narDjUG+muks5e7cpmWF2Kja7I/L/dZb8n2qY+Vj3Yq9MgA33LKOLWsYpNvCTLXal68d51p6Lx1bntil74+V/ddwbd4/GC/+VpT78sE4YGNN3nerNtd6n22Daxkr/ahbcdgfzkrHbFOVJjWGojRZh1RDrMJZSbbtZ5nlMWVZx+Y23CloqWebLEffMhTOUgzX6dhyDgAr7Zprzml71srEtNiPrvXGtNz1fl8eB9bp2FKXWZs7Te9+dKxcQECaA4ejcgyXY2Gq1Zzqeqs2tCs2t5bmBcuaWHfMlRXAjYpd2pGwzob1OmZzPC37r+HZ3DjO72ddv2qt0ax1x5bHQ9c01vblZT84a8fypflExSktIhhKrbW1mItHk3DtuL3OhqIG92flhatiu+VCs7mmECrmwP44XDsP2ag6XC/o2HLeQKpjprGqpUU/mMaqXiyPRQ+bim2s+GV5LP868rCtuwHc0Fr/Kvv7PyMtdhZorf+O1vplrfXLW1tbD9mcB6NuGzy1la/8mYbixdNtrh7mRUTdMTnfqvDeYS4gFzsV6k4+qBgKvnW6SdPOM7xq2zy6UaVW6KTbNYe2Z1PUrGd3GiSFWfB8//+gMHluuhZnmhXeuJVPCDUJz+82Sja8eKbFUWESPA1jntyqlwR3t+7SdEx01lCR7rctDmC2qfjGqSZv3ewtjt3qT/nW6VYpERXw/E6+Am8qePlMi1HhCU/NMbnUrXBUOHauVaHhWgvbFfDCqRYW+eAbRAkXu9XSU4bNqsN2zS0NFs9s10udfP4O0Y3CdoTBLOL5U83SgHWpU6Fml2P4wukmh4XHz55l8NR2fbHfHGCn5tDyrMXqrAKe322UntrZ2Xs47+33F8dansWpukt/lt/jo90qlsFSP2pxu1DEVm2TR7s1PjzMhfRM06XpWQtBUsA3TzUZznI7HdPgG6ea/O7OYHGsW7HZrrulsfbJzRqekR+JYs1G1S5N7OuOycV2pTTBPdfySjmgSG2f+nm/PZqFXOpUS0XxVs2h6zkUdmtSsVRpC1/6HlOLjw5Gi2NN1+Jsq1KaCF3sVHFMtZIDxVhULIMnN2ulxYLdupuuWhb89/xuE1Pn9zcKYk43PZqFQqXt2ew2vNKk47GNKk4hJ7ROB9GtwpO9mm3yaLdaWs080/RouGX/ffNUEz/I/eeYBs/vNnjrViGGVZutql2aXGqdvjswZ65jHx/kfabhWJxrVRj4ebsLbY+abazo2MwvT5ae3q7zxs3chu2aQ6di59u/ANdSPLqRr2LP30V7b6+3ONbyLE43vdJ2JfR6Hbs7LOfA4xu1UlxPNVya7pKOnWqiCzEcBBFn25XSCnWnYrNdd+gX/IDWPFPYgmuqVINvF7bD1ByTi90KNwtPgs61vFUdO92iV5iAuqbBszsNfnot98OtwYwXT7dKhd+zO+t17Hov90PDtTjXrmRbpDJ/6ZhvZu/rzP33rdMt9gv+8yyDp7ZWdazpWaUYPr/TwI9WdaxYxM5jWFyRfrRbpWLl/WgSQqdisV3IgbmOXSv49HTTpeXZJR174XSTqFDMO6bBc6eaDAvjR7dis1N3KZZ9T27WsFVZxzZrqzp2oV3hnb08L861PBpLOvbC6RZHhSLMtQye3mkwKoyRWzUnK/pzG57daaAL2jDXsfcP8txpuhZnWh6jQl++2Cn7z8jG0WLxVrENntislXJnt+7Sck3Cgv8qlsGlwlNJ21B881SLq0f5Pbc9m9NLOvbkZq20QGdmeXirn/9ezTF5ZI2ONZdy4JunmvQm5bHo+d0G7+3nen7leMKLZ1qlgv6prTqVwpw+SDRbVadUXDQci/OdSunJ2oW2R3VJxxqOVdoGN9exH185Xhybz8eKOfDcUg5Mw5jdhlvaMdDyLE41Xd4r5OEsjNfq2O1C8Vu1TR7bqPF6YR63P/T51ulWKQe+capBw/3qCouWnfbT5Rxo2auLZl8nlF6q/r/0H1DqJ8C/qrX+QCn1N4Ga1vp/te7cl19+Wb/22msP1Z4HpT+LmAQRsyim5ljUjZhAWQz9mERrGo5Ft+ZwMA4YBWH2hR8Ty4ChnzANY6qOlX75Zc3LV0eTIHuJPf1KmGckDKJ0O4ZnmdRtE03CKNT4UUzdtdiquRxPAoaZuDWc7OtbfsTIj3Asg6ZrMfVjJnGc2mCbtGxQVrrCGSeahmtRcywOxj7jIPval2NSdy16k5BR1q7j2UzCKNuSl1B3LDZrLtMwYjCLUErRdC0822R/5DMKovTrOo7CNk160wg/iqk5Jt2KTd+PGQep/+quxUbV4WDsM8q+llZ3LCxTM/Y1kzCialvUXIVOVLoPPNE0XYtuNf2y1+JraZ5FxYSenzAKIjzLTCcuOmEQJKn/HIutusvxNGA0j6Fn0a3MbYjSL6w4JpYJgyyGNceibkMQG4zC1H9112Qj+yLOKPNfzTGomYpekO7r9WyTpp1+XWgS6ZINR5Py19K6Vafkv5qlMJTBKIqZhan/mhZMtWIcJJkNqf8OJz6jwhfbTDNhGsI4SLeuNFyDIE4fzxdjWOx/ddfESUIm2lr4r+oYaBKmgWYWJtRdk5qR4GMwCtIvBjZdk041/TLVMIixTYOapbAsxTjQTIKYqmNScxRRrBmFmihOr7VZS78MlL4ArWg4Bq7SDCO18F9dabSV/p4fpe226h7Hk9TvidY0HYtOLf2i0OKLgSZgwDRSWQxNWo5iGsEoTIiThIZr0c2+iDPyI0zDoGYbVC1NL0j9VbFNKlYCiWIUp08pF/1o7DPIbK876Vd/9oczRkGMZxlUbIWpNKNQLWLYsDS+VgwDTaIzG6ouh+MZQz/d7lS3FaapmBT8V3cSwshgHGnCOKHhmGzUPY7Gqd8NpajbBq5KGCcGIz/Gsw2q2SA0DjV+mFBzTepGQqANhtlXHxuOSbeWfllplPmvaoFjaYaBwTSzoeooohDGcUIcJ9QXNsxjmNpeMdO92osY2ppYG0zCLIaeyVYtjeEwiEFnOZDFcBREOKZBzQYDi3ExB2yYxip9B0CnsdiopV9WGgVpDOuWQcWO6QfpFq9FDLViFEGYxXCz7pb6X902s340Y+THuFZ6LWUkjMJ0i1/dMalbmlmiSl/N3Ki7HIzTdvY8hknEWFt5DqiISFmLGM5z4HDkMwozGywDz9SMIpX2I9ugYSgSpRhnW4sXOTD1l3TMLcWw7gBaM42MQg7ETEOLUZTmQN1JbT/M9M9UaQ5UTF2KYc3WJDFMYrI8zHRs7C8m4/XsS3LzHHCttP+ZpPdTimECoywH8hjOMi01qFkGlhkxjcw0ho5Jw4gJMJisxLCYAyYOEWNtMvZjXDvVI22w0LF5DvjaWMSw6Zh0aqs6ZtsGIz/JY+gaRFHy4DpmK2KtmYQ69Z9jstW4Dx2zAZZjmDCNzBUdOxr7DEs6Br1MQ9IcUJAkjOLUf7UvRceSwlwoz4G5jlkqYhzlOVA3YkLMFR07Hs8YLOnYKDEYz3XMUKBgHJd1zNcmozD+bB0jYZiYuY5ZIVHs5DrmmmzU7kPHlCY21SKGDTfXkJUcKOqYCYYJ41B9ro4dZf3PNBRNC1zbXIqhSWvNroGHySQIGBbmYw1XUXVWn3z+IVBKva61fnnl+FdQ3LxA+iloB/gU+Je11sfrzv06FjeCIAiCIAiCIHy9uFdx89A/Ba21fgtY+WFBEARBEARBEIQvk6/3G0GCIAiCIAiCIAj3iRQ3giAIgiAIgiCcCKS4EQRBEARBEAThRCDFjSAIgiAIgiAIJwIpbgRBEARBEARBOBFIcSMIgiAIgiAIwolAihtBEARBEARBEE4EUtwIgiAIgiAIgnAikOJGEARBEARBEIQTgRQ3giAIgiAIgiCcCKS4EQRBEARBEAThRCDFjSAIgiAIgiAIJwIpbgRBEARBEARBOBFIcSMIgiAIgiAIwolAihtBEARBEARBEE4EUtwIgiAIgiAIgnAikOJGEARBEARBEIQTgRQ3giAIgiAIgiCcCKS4EQRBEARBEAThRCDFjSAIgiAIgiAIJwIpbgRBEARBEARBOBFIcSMIgiAIgiAIwolAihtBEARBEARBEE4EUtwIgiAIgiAIgnAikOJGEARBEARBEIQTgRQ3giAIgiAIgiCcCKS4EQRBEARBEAThRCDFjSAIgiAIgiAIJwIpbgRBEARBEARBOBFIcSMIgiAIgiAIwolAihtBEARBEARBEE4EUtwIgiAIgiAIgnAikOJGEARBEARBEIQTgRQ3giAIgiAIgiCcCKS4EQRBEARBEAThRCDFjSAIgiAIgiAIJwIpbgRBEARBEARBOBFIcSMIgiAIgiAIwolAihtBEARBEARBEE4EUtwIgiAIgiAIgnAieOjFjVLqilLqHaXUW0qp1x727z0Moii6r2NJkjzwOevOu9/fW3fsi9i57rw4jlfOWXdMa71ynS96rfvxw8P23/1c64va/nWw4X7bfR1s+Lxz7veY+O+vduyk2SAx/KffBonhX80G8d8//TZ81XwdbHgQrK/od/5Ea33wFf3Wl8bh2Gd/HHBzMKPpWpxvV1BKcb03pTcL2W24bNddwljz6eGYMNE80q3SdE0OJxHXehMqtsnFbpWKaXCtP2VvHLBVczjXqhBECZd7E6ZBzLl2hY2qxdBPuHw0wTQUj3SruJbB3ijg9nBG27M516qA0lzrTenPIk43PbaqDpt1d8X2w0nIjf6UmmNxoVOhYiou92ccjgO26w7nmxXGUcyV4ymzKOZCu0rHs+j7MVeOJzim4lK3hm0q7g597o58uhWbs60Klqm4cjThaBpyqVOl49mMwpjLR2MALnVr1B2TvXHAjf6UhmtxoV3FUHCjP+VoGrJTd9lpOIQxXD4aE8Sai50KTc+mNw252pvgWQYXO1Wqlsn1wZS9UcBG1eFcyyNMNFePp4yDiLOtChvVuQ0TTKW41K1StQzujgNuDWY0vSyG5DE81fDYrjv4UcKnRxPiRHOxW6XpmBxNQ671plRsk0vdKpZS3BzO2B8HbNccTjU8Iq25cjRhGsacb1foVG2Gs9R/lpHbcGvkc2fopzFsV9Bac60/ZTCPYd1hFqQ2JKT9qOFY7I8Drven1LMYOkpxdTDjaBKwXXc5XXcIErh8PMaPNBfaFdqeTW8WcrU3XcSwYmpuDsNFDM+1PGINV3pTRn7qv82awyTIY/hIt4ZnGxys5ADc6M04znJgp+bix2m/DZM0hi3b5MiPuNaf4lkmlzoVXENxY+izNw7YrNqca3iEGq70JkyCmHOtLAeChMvHeQwrpuLuOOT2cEbLsznX9gC43pvRn8ewZjOLNZePJsRac6lTpeEYHE4irvenVB2Ti+0qloIbwxkHkzCLoUuUwOXjCbMo5nyrQte16IdpXthZHlZNxc1xwJ2hT8ezOdv20Bqu9aYM/IgzTY/NmsM0TLh8NEYDj3Sr1GyDg0nI9f6MumNysVPFAq4NZosc2J3HMMuBNIYGvVnC1d4U11Jc6tSwDLgzCtgb+XSrNmebaQyvHk8YBTHnWh6bFZtRlMZCkdlup/5b5ECrggKu92e5jtUcgsx/0TyGjsnhLFrkwMVOBdswuDWcpTpWdTjdcIm15nJvyjRIc6BbsRj6MZePp5+pYxrN9X6mYw2PnZrFJEpjsYihpTiYxZmOmVxoV7ENuD6YcTiPYdNNNeR4zCxKuNCu0HEt+kEaQ8dUXOpUqRhwcxyWdCzRqYYMg4izTY/Nms0k1CUdq9qKg3HIjcGMRpaHhlJlHau5hEnab+c61nJMjv2Iq70pnmVwqVPDNeHmIM2BjarNmaZHnMDV3oRxEKc6VrEYhYUc6FSpWLA3jrg1nNHyLM4txfBUw2O7auMneqFjl7ppDhxNsxg6WR6iuDb02Z8UdCxJuHI8XejYhpf7b65jrqm4m+VAGsM0D68WdGw7y4FPjyZoMhssg/1pOQcMBTcGM44mIdt1l1NZDlwp6VieA3Mdcw3N7VEhhk2PBLiS5cDZlsdGxWaa6bnKdKxuG9xZ1jHgRr+oYw5+lgOfpWOeaXB9MMt0zOFMyyOOda5j7TSG96VjOo3hXMd2ajbTdTo2jbjey3XMMVINOSjkQBRrLs/H8laWAwUdu9StUjMVN8YBdz9Hx2ZhwqeLHEjHsINJmgN1x+JiJ/XfzWUdi/UiB+6lY7aRcHsYsjcO6FZtzjfTcWBFx8KET48nGJmO1WzFnc/RsVM1Z+G/uY41HIvjWVjSsbphcLmoY02PWCdcPspzoFOxGC3rmKnYy2I4zwENpbF8p2ozifTn6phrwNWijjVcwmSNjvkxV3q5jnUcqFQqD3HmW+ZoHHA8m8/HUv+dbn51v/9FUcsr71/6Dyh1BXj5foqbl19+Wb/22tfj4Y4fhrxzd8THh5PFMdcyeOlMi59fPV4cO9fy2K27/OZmH4CGY/HIRpXf3h4szjENxXfPd/jplaPFsY2qTdO1uHw8XRx7frfB0A+5cjwDQAE/uNjlJ4V2Vdvkm6ca/OJab3HsUrfKN3brVGx7ceydOwPevTtc/G0bih9c7PJPPj1cHPvBxS6/uHpEXOgC3zrd5FZ/yt1xCMAPL3b55HDCreFscU7dMfnOuTb/+JP8Wk9t1bk5mDH08+r++xe6/OxqbvufPrLBb270GQb5OacbLhfaFX5xPb0f21Q8v9PgjVsF/yn41ukWr2U+Bmh7FhtVh0+O8vg8t9Pg06MJkzBe+O/Vc21+dT33lWcZvHi6xc+v5TG80K7w1GaNf/Rx2kW3ag67DZd37uT+swzFN3abvHErt2GjavPi6RZ/nrWzDHjxTJtfF35PAd+/2C3FvmabnO9UeG9vtDj26EaVtmvy+q38N797vsOvrh0zf1Zlm4rvne/wo8v5tU41XBSqFJ8Xz7S4fjxhf5LG0FDww4sb/OhyHq9vnmry3t6QoBD8p7Zq1Ex4/U46qD2zWSXUio8Ox4tzXNPg5bMtflbIgbMtjyc3a/xXhf7wytk2b93qEWbGmyrtf0UbfnCxyy+vHRMluQ3P7zb4+GDMNEoW/vvexQ4/u5L/XsUyeKRb5d2C/y52qjy1WeEffpRev+NZnGlV+N3dcgyf323yZiGGm1WHF083+bMshrYBL5xu8Zsb+TkK+OGlLj8u+L3mmHzvfGcRe4DHN2qM/JDbo2Bx7HvnO6W+5piK71/s8k8KvjrVcLnUqfDzQk6/dKbFx4dj+rM0V57drnM4Cbkz8hfntFyLrbpT0qhntut0bMXPbub3/f0LnVK8/vTRDX51rcc4zFcMz7U8nt6s82ef5Pfz6rk2b9/ukZmAaSi+earJG4U87FZsXjnT5B99fJj5GF46U865e+nYd8+3S33mh1meFEeklRwwFN9e0tLtmsOz23X+SRYfxzT4xqkGrxViaCj4wYUuPy60+/6FLr+50SOI86fB63Tsexc6Jc13TINXzrZL2na64XG+7fHLwn2/crbF7+6MmEapn00F373Q4aeFvtzyLB7fqJW07dmdBrezSePcf+t07AcXuvzjQrx+kOlt0X+vnG3z+s0e8xSzDMV3znX4acH2zZpDzTa52svHohdONXlvb4Qf53n4ytk2v76R21CzTZ7fbZTu+fGNKnvjYNFvIc2BX107Zt7bXjnb4oP9MYOCj1Mdg1vDvH+/dKbFu3eHzDItMFR6rJibTddit+7wYSEHntqqcTgOFvo3903xnl3L4PsXuvxFwX9nWx6Pdav8ZSHPXz3b5r29HsMspdfpWKdi881TDf7y07SdQRqvX35ODlRsg+9f6PCPP86vdalTpeWavJWNPRfaHg3XXtGx7yzlwGbN4aVTzcUY5hgG3zzd5DeFeK3TsT99ZIOfXT1exBngiY0awyUdW9aQV862eH9/XMqT0w0XDdxeiuFvbw8WGp+ORd3SGPb9Cx1+faNHWBiLnt2pc+VoWtKoZRs8y+DxjRrvFHxzsV1hFMQcTHLbv32uzW+XdOyHF7r8ZSGG3YrNS2ea/HkhFt/YbdKfBVztpWPrpU6FOCsE51TtdBwo5uHyvAdSHXv92jFzq2xD8cNLXf6ioH/bNYcnNmv8NLtHxzT4xm6jpA2GSvvRV1lcfLA/5M2l+dgPL22w2/C+Mhs+C6XU61rrl5ePfxXv3Gjgz5RSryul/vpX8HtfCgM/Xfkp4kcJflTeFnW9P6Pm5g/Antyq8eHBqHROnGiGflRy9uEkpOqUH5x9eDDmsW5t8XcqFDOe364vjk3CuCQCAFeOJoz83K6jSbBiQ5jo0oBjG9CfhSxdio8Oxjx/qrX421CUJs4AoyBmFMRL7UacaZY7+5XjCf/CU9uLv6dRUipsIB3MHCv3zOmGx4cH49I5sU5/01Rqcaw3i/Bss3TeB/sjzrZyGzRwZ+jTKPh5FiUESfmmr/WmpWNPbdX5aMmGKNGlAQDSGE4L4vvYRo1PDsvtNLA39Gl7uQ3jsHwvAJePJrQ9Z+XYhU4uYmGsV/x+e+jTqdqlYx8djPlGIYaJhoOxT7dgQ5ToUmGTtpvQref+221W+eSofD9+nCwmG3Nu9GfESz79+HDME1uNxd+x1vSmIU4hZOMgKhU2AB/sjznbzu9ZA7cHPlu13DfTKIEl/109nuAXXPP4Zn2lH6X3XLb9YBIwifKGT2w1SsXC3Ia9kc8zW9WC7XFpYAf45GjMxW61dOzK8YSLhfsJYs1wVm53e+hjmWUp/uhgzAunmou/G55VKmwA+n6EZ5Vz4MODMdVK+Snujf6MU4382DiIS5MGSHUs1KsxfPlMZ/F3nGhmYULR80fTkHGUt3u0W+OTNf5bp2PFvvzUZo0b/SlLcsSnRxMeKfg0TDSTpRzYGwcUTOCJzRofL8U+0bA/DnhuO9fXWRSv9Id1Onb1eMq5UgwTZlHZhlvDGa61GsNvnCrmAPSnEXbhtP4swljqyx/uj3h8szwO3Bn61AvJM4sSBn4+ed+o2NwZzVb8d/lowlYtj32UaEZhuf8djAPqbnks+uBgxJklLT2cBHiFexyHMfFSn/nkaLLiv0+PJzxdiL1ClQobmOtYWf8+PBjz1FbeLtGpv2wj99fAj7CXcuCjwwmPbdZLx672Jvzxxe7ibz9KGM7C0jk3+uVxLr3WmO+c31j8vdCxgruOp2FpTH5so1padIPUf7cGMx7dyPvyNEwY+uV+dOV4UvLDoxu1tTo2DlZjWNSxx7dqfLxuLBr5PNLJ4zPwo5Vx7eOjMRcL8xBI+9GfPLJROKJW9O/W0Ke7FMOPD8fsFrQn0em4eaqo52GyMqf5YH/M2VZ5Ar+sY7MooWx5uhNhp1HWv48Px7x0pr34O040fT+k2GuOpiHTqGzDhwcjHi/0o92Gx/VCYQOpjhXnNLt1l5uD8jmQ6tgPLuX9b3k+BqmOqYIWPLlZKy0sQqZjhaLzYdObBmvnY0eT8B4tvj58FdvSvq+1vqWU2gb+XCn1vtb6x/P/mBU8fx3g/PnzX4E5fzUUaunvMolePWfdeeuOqTVHFYp4echaaqjUmmMoWGpXHEP1PW1Spfdo1p2zfK31B9K2yfJoex+oNddK+eyLKbV6RnrsQY3Q97zv1d9ccuq6lmvsWvurS/f9xWxnTeTTiyVL56w5pXznar0f1vpm2XYgWX4qvOSHtXmiYKWZWr3Wvez/rL/v2a5wNNH3vuflAm65nyoU6OUYqpUBeB3r0ql4y+t8dT/XWVzri7RD3Zff1/3eumtFn7FLIP2d9RqyPIFem2IrsV/ft6Ll1ZzPuxDzWHyBPFRqbV9ep1Er7dbZsOb6c5J7KPo6Dbm/sWid7at2rWP5HIOy/+4l7+vGw5X+dx82KNZpiFqJ4Wr+rhq3oonZseQzXj9IuIePFSSf0/9W+gLq/nWscKK+p46pko6tzRPW9b+yFtz3+MhqLAwFYZw78F73t9Jv140Na9qtTpdW+/L9cP/3eB/jxxoN+bzra9bHx7hfw74ElL6/sfbryEN/cqO1vpX9/z3g/wO8uvTf/47W+mWt9ctbW1sP25z7puUaPLZRXr2o2AaOWY7qhU6V4SyvpD84GPLkVrmdbSjqrlWa5GzXHEZLKx9PbdX5YD9/xGqo9HH97/fyyrnmmFhLPeuRbo2ak4eyW3VWbHBMg5ZbXLmHlmdjLWXKE1s13ipsqQsTvdhbPafpWtTscl381GadG/3yisXFbpX/4oO9xd8Vy6Dllduda3mlpx83BzOe3CzbbhmKhmuWnjJtVO1SO4CnthrcKKysKGC37pVWiKu2ibN0zxe7VdzCMs7v7454cqu88mcbqrRqCWkM3cKK+8dHYx7fKK/cGwp26m5plabhmCsTtse6NQ5HZf9d6tYWWxQh3RLWWFphPdvyOJqUV3Ke2KqVtg6ZSrFZtekVbLAMVlaan9issT/IVxxvHE9KK8iQbgVwltqdb1dQS4PH45s1Pio8PbQMRduzKYasuiafntqqc71fjuGphsdhYaWo5pgrA8UjG1WsghHv7494cmn11jHVyu/t1F0qhaX0jw5GK/dsKNiqe3xwmNvVcC3qTtkPj29WF/vU51zsVEvbGFzLoLkmhv7Sk4AnNuu8cTPPw+NpwOlmeUWyW7GZLeXAk1t1JoWVRAWcbVW4U9gqUnPM0lMASHXMWhqwHt+o8tqt3uJv21B4tlGaO2zVHKpW0X/j0uo05Dr23n7um7pjlvryh4cTzra8lYH0kW6Vq4Wtu45pULXLfj/VcEsD2Qf7w5UYmiq19f3CUyXPMlZy+qmtso4p4GK7WlrVX9duWccgzYG3bvcWf1uGounZFB98dis24dLK+ZNbNT7cz3NnrmPjJR1rFGJ4PI3YbbgrE59Hu9XSSq9tKOpLOwZ26g6DpacY6fa83A+GSjW3uHOh4VgrT52e2KyvPAG51K3xbiH2caJpV8pPm8+1PA6XdOzJrRofFFaNTaVouVbpaW/bswii1Rz46LDsvwvtCj8ubGmqWKtaer5dWflgzeMbNX55Ld9yZBmKdsWmOHJvVG0sI+8Pnx5OeHRp7qBIdyV8WtCCmmOWdhVAusX8cJz77/394Vodqy7tWtitu1QKffLDe+jYdt3laj/XgoZrrvTlxzerfHpY3vlxsVMtbSXT6DVjeYWDpafLj2/WS9pjGopu1eFglvu5YhmlcRTgqe3VceBsq1J6er3sA0j9d2dpp8ljm6s61vZsir1mq+bgLdnw5Fad9+7mGnyrP115Ml93TOqFycPeOOBM9i5QkUe6NX5c2I7qmKvjwKmGW+p/H+wPeWKtjpXHgYdJq+qszIUsQ9FZyt+vIw/1nRulVA0wtNbD7H//OfC3tNb/cN35X6d3biB9DH80Cbg9mNH0bE4308H39nDG8TRkt+GxUbWJ4vTl8DBOON+uUHctjqchN/szqrbJmZZHxTQWL6Nv1hxONzyCOOFGf5a+SNr2aLs24zB9+dMyDM61Paqm4u4k4s5wRrtiZ49lFbcG2UuITY+NisNGrfw4+HgScJTZUHdSGxzT4NZgxsEkYLvmcqbpMokSrvenzMKEs+0KXc+in71E7FgG51oVbBMOCi/i7jY9HMPgej99Kf98u0LLMxn5yWLf9oV2hbpjsj8OuTVIPyhwpumhDMWdbD/5dt1lK3uR+UZ/ShAlnGtXaHsmx7OY670pnp3aULEMbg199kY+G1WHM83UfzcHM0Z+xJlW+iLzKEzbGUpxvl2hahrsTUNuD9KXOE83PUBze+jTy2K4mQ3a1/szoiS1oWlbHPkhN3ozapn/LKW4O/Y5yGK4XUtfpr7ZnzEJY860PDoVm6Gfvvw5j2H6MnDMneGMTsXmVMNbbFMYZDHsVm1mYcK13hSN5ny7St1OXyS92Z9Sz/xnGorbQ3/xQYFTdYdplPpvNvefa9L3Y65lLzKfbVWoWwY3Rqn/uhWbU02PWGtu9dP3C0630thPooRrvfRl9PPt9CMUh7OI24MZDc/iTMNDqXQbyXH2IulW1caPdbq1aZ4DtkE/iLnRn1GxDc60KrjAnUnI/thns+qwW3MI0dzs+9nL1B5tx2Qcp34wDcX5VoWqqdibRouXOE83PbTOYjjL8tCzCZKEa/0pcaI5365Qswx6fmpDGkMXC8XdScDBOGCr5rJds4l0+pGLaZgsbBhmsbBNg/MtD8fU7E9i7o78LIYuWsPN4YzhLErz0LOYxroUw5qlOJxG3BrMaLgWp5seBnBnHCxiuF2zsxyYMYtS/zVtRT/UaQ5kMXQM2JuE2QcFHHbrLonWixxYxDBMuNbPY+iaiuMshk3P4vRSDHcbLhuV1Ibr/SlRrDnXqdCwDY79uKRjtkptz3PAIUnSl8PnMex4JqPMf5ahONeqULXW6RiZjqUfFNiuWoyjVEsTrTmX9dsjP+Zm9mGUsy0PQ8HdUcDhZB5DhyjRXB+kOnauVaHjmvSDNAccM83Dpqm4Ng4XObBbd0kyG4Z++jJwxzOZxZR0rGLC0SxejeHIz3WsYhNqzfXejCDLgZZjcOyn+urZBueaFRxDcWccsD9OdWyn7pBouNmfMQoyHXNNRlE5Bzwz60fZBwVON9OX0Ys5sFOxmCSpDVGS5+HxLM+Bs00P24DbhRju1ByizIaFjrlpDlw/nmKZaQxdEw6mUfpRjUIO3BrOGGQ50PUsZsUcaKU6djCLuJV9WOZ008NQKvXfPAeqNkFCScdatmIQ6oKOeXhm+lL5cg4UY9itWEwifU8dm+cAKt3uV9SxINZcK+hYwzboFXTsbKuCZyhujdIYbtYctusuSaLzsXydjrUrVJXi7izLAS/1n1LpWL7QsYqV2VDQMcegNy3qmIedachBlgNb1bTgulnQsZaT5+GD6Fg3y4GyjsHh9HNyoGYTLulYyzHoBUlJxxoGXP8MHZuP5eOgrGOeqTjKxoF76dhWJf2wzPX+lCjRnGtXaNiKYz8p6Zir4NaSjsVZDsxj2PXyccAyFOfaFVzD4GAa5mN5PX3PaJ4Duw2PrUo2DpR0LP0wxc3s40Bn7lPH2q5BP/PfXMdOfcUv8/enAUeziBuF+djX5X0b4J7v3Dzs4uYR0qc1kG6B+39prf839zr/61bcCIIgCIIgCILw9eNexc1DfedGa/0p8M2H+RuCIAiCIAiCIAjw1XwtTRAEQRAEQRAE4aEjxY0gCIIgCIIgCCcCKW4EQRAEQRAEQTgRSHEjCIIgCIIgCMKJQIobQRAEQRAEQRBOBFLcCIIgCIIgCIJwIpDiRhAEQRAEQRCEE4EUN4IgCIIgCIIgnAikuBEEQRAEQRAE4UQgxY0gCIIgCIIgCCcCKW4EQRAEQRAEQTgRSHEjCIIgCIIgCMKJQIobQRAEQRAEQRBOBFLcCIIgCIIgCIJwIpDiRhAEQRAEQRCEE4EUN4IgCIIgCIIgnAikuBEEQRAEQRAE4UQgxY0gCIIgCIIgCCcCKW4EQRAEQRAEQTgRSHEjCIIgCIIgCMKJQIobQRAEQRAEQRBOBFLcCIIgCIIgCIJwIpDiRhAEQRAEQRCEE4EUN4IgCIIgCIIgnAikuBEEQRAEQRAE4UQgxY0gCIIgCIIgCCcCKW4EQRAEQRAEQTgRSHEjCIIgCIIgCMKJQIobQRAEQRAEQRBOBFLcCIIgCIIgCIJwIpDiRhAEQRAEQRCEE4EUN4IgCIIgCIIgnAikuBEEQRAEQRAE4UQgxY0gCIIgCIIgCCcCKW4EQRAEQRAEQTgRSHEjCIIgCIIgCMKJQIobQRAEQRAEQRBOBFLcCIIgCIIgCIJwIpDiRhAEQRAEQRCEE4EUN4IgCIIgCIIgnAikuBEEQRAEQRAE4URgfRU/opQygdeAm1rrf/6r+M2Hxd5oxiiIcQyDumOhDM04iJmFCVXHpO4aBBGMgog40TRcm82aw/7IZxREmIai4Vg4Fgz8hGkQ49kmFdsEnV4rSBIajsVW3eVw7DP0I5RK21WMmGFsMPIjXMug6pjYCvp+jB8l1ByLTsVkFMQM/ZhEa5qexUbV5XDiM5hF2KZBx7OIYxhHMdMwpmKb1CyTmIRhkBAnCXXXYquWtzOUouGa1EzoBTAOUhtqtoFWikmQ2lB3LRpmwjQxGQYRWmsarsVGzWV/5DMMIhzDoOZYoGAaxszCmIpj0sz8N8z8V8/8cDAOGPrhwn8Nz+JoEjIOIiq2ScezmIaaURARJAl1x2S77nE0CRjMQpRS1F2Lpq049uM0hqZBwzHRiWYSJcyiNIYNRxFEKrVBa5quzUYhhpahqDkWJoppFDPJ/Fe3TSISRn5CmCTUHYvtustBFkNDKequSc3Q9CPFOIth3THRWjMOkzSGrkXL0kwTxWAewyX/2YZBzTWwMRiFaQyrtknFMol1wijMYrjwX9kG24RJoJkEMZ5lUM1iOA5igiih5pg0Lc0kVozCpBTDvWGWA6aiZhkoYBLr1H+2Sd2ICJTFKEiItabhWGzWXQ4y202laDgGto4YJRaTMLPBVGgN4zghiHUaw4a3lAMGFUMziFJbXdOgagMapjHMMtsrVkAUuwzD1H8N12Sz5rGf2W6aioZtYKiESaSYhgkV26AGxGbq0zBO223VPQ5HMwZBnOaAY1I1A/qhndpgGdQMjVKKUQR+nNrQsmEcwyhI/VfP/LA3mjHyY2xTUbdMLJ0wSmCa+c8zYxJtpjHUeQ7MbTAzGywdMtbWIoY1S6GBUagJ4jQH6lkejsIYnfUjT8WMYmORA3VboYBxtBxDm1EQl2K40DGV+k+pmGlsphpiGXgGoAzGUUxQ9N/nxLBipStt45hMx0zaTsA4zGPYdEw26mkMh0GMlcXQjBPG5DGsWppEGwzDhDjrR1sNj8PxjIGfxdA2qdk+vcBZxLBqpho/KcSwmeXhMLj/HKjYJk0zJtBmasM9cqDumDg6LOVAzVTEwCTKY7icA3XboGIkKzEkazfXsZqjiGIY+nGmYyYbNa8Uw7pjYKqEaWSkOmYZ1A2IjDwH6m6qpXPb8xzQ9EMW/qtn/hsVYtiyYRIrhsE8hhYbdZf90YxhlgM128ROEkYapmGS6VhCrI00B2KdjkV1l4Nx2m5ug20EjCM71zEr9UMxBxqZjg2DGGBtDKuWgQmMv4COOcQMY7OsY8A4SnWsseh/n6Nj2WxsUvDf5+mYZab94Yvr2Ix+6N5Tx+qOSdNObZrnQNO16NZyHXMyHTO/gI7VHRM7CRhj35eODcM0hk3H/Hwdc0xqhISGU9Axk836Ug7YBsaSjtUNiJXBaEnHjsY+g6UYDiPFqBBDpTXjRH2+jmX+m8fQjDVjyGNoaeI1OvZVczwJFvOxhmuxWXO/chu+CF9JcQP8a8B7QPMr+r2Hwo3+lF9cPSbWGoDzLY/HNmr8+PIRAAp46WyLJE544/YQANcy+O75Dj+/ekwQJwBs1Rye32nw408P0dm1n9tp4Fnw2s20nWUovnehw5s3+wtRbroWL59p8ZeXD0iyho90q1xsV/jJldyG75zv8PHhmP1xAEDFMvjO+Q4/vXJEmDX89pkGfqJ46/ZgcX8vnGriKM2vb6U22Ibiexe7/PraMdMotb1dsfnWqSZ/WbD98c0a55oOP7lyDIChUhuuHg25OZwBULNNXj3X5idXjogyG861PE41PH59o7ew/VtnWvQmPp8ep+0c0+B7Fzr84toxfmbDRtXmhVMt/sknBwsb/tqjG3x0MOZaP21nKsV3L3T4/d0+R9NsUHMsXj7b4seXD4mzhs9u10mA9/ZGCxtePdfm6vGUOyMfAC/z38+vHhFkDbdrDs/uNPjR5dwPz+82sJTmzdujUgzfutFnkIlyy7N46UybH32ax/DRbpWLbW8RQ0PBq+c67I9mfHI0BaBqm3x7yX+nGy7P7NT50eXDPIanm6gk5s074zSGpuL7F7r88toxs8x/3YrNszsNfnrlaGH7k1s1tmsuPy3Y8MePbPDajT5DP0pj6Ji8cja1IS7F0OXXN/oL/714pkUQzHhnP7XBNQ2+e6GcA5faHt2ayxs3C/7baeDHMR8eTNIYGorvne/w9p0+/Vk+MXnlbIsfXT5c+O+HF7vsjXw+OBiXYnhzMORGP4/hd5dyYLfh8kinys+vHS38943dJg1H8bNr/UUMf3ixyy+vHzMNsxzwLF48U7bhrz3a5crxjE+OJgv/fftchzAMeS3rD3Xb5MWzLX5+9XgRwzNNl6e36vzoyuHC9j+6tMF7e0P2svx1TMX3LnTLOVCxeWanwU+v5P57eqvObt3lp1fT+zEV/PGlDX5945hRpiH1LIY/vnyU61jb4/GNGj8uaMgfP9Ll7dt9jiZhGkPL4HvnO/ysEMPtuY5dLuvYdtXmp1ePF/5bzoHtmsOjGzV+df2olANNz+LNW4OS/z4+HHymjp1uuFzoVPjFteNFDF841WQW+ryf9aO5jv2qkAPtis2Lp8s69tce3eDT4ymXCzH8zvkOnx6OF1pQy/Lwx4U8PNvyuNiuLvw+z4E4mvHW3XEWw1Ud26w6PL1dL8Xw2e06ida8l+WOqVL//fZ2n4Gf69hLZ1v8pKBjFzsVNqoOr9/M83Cdjn33fIefFXRsJ9OxvyxoyDdPNRn54UJ70hh2eeNGj1FBx1441eQnV8ox3K07/OxarxTDWRDx5p10TFmnY89u1zANg7ezcwBeOtPiYDzlai/Vc9tUfO98l19dz2PYqdi8cKrJjwoxfGa7jgLezfTcVPCd812uHA65OUr7Ud1Jx6IfFXTsm7t1oiRvpzIbVDzlN3fS/uBmMSzmwFbV4cmtOj+7Ws6BIE74MNMj01B8/0KHN2/1Gfr31rFHulXansUbWQ7MY2iriF9kPvUsg2+f7/Dzoo7VXZ5bGgf+a49u8O7dIbeHaextQ/HdC13euHHMqKBj3zjV5KdXchue2KzhWXksDAXfPd/lvb0hR9PwnjE80/R4fKPKjwoa8q3TLfrTMZ8sxvL717GzraKOKf7oUpffLOnYy2fb/KSgYxfaHhfa1ZKOvXy2zf5ozJVe2pfvpWNPbNZKMXx+t8EsjPnoMI39XMdev9FnHC7Px8ox3K46/PJGPhf640sbvHmrR2+WjqPrdGy37vLEVj6XBPhrj27y7t3hIn/tLA9PNb+6AudgHPDb2/2FBs91bPcPUGQ9KA99W5pS6izwzwF/92H/1sOkNw1461Z/kUgA1/qzhdACaOCtWwM61byy9aOED/fHPL5RWRzbHwcMghi7cP137w6p2PmRKNH89vaAdtVZHBv4EXfHAS0vr0k/PZrgx2UbXr/Zp1PJrzWNEi4fTXj1TGNxrOI6vH0nL2wA3r4zoOblvxcmmt/dGfL9852CH0IOJyGOlXedjw7GBIla/J1oePNWnye2aotj4zDmWm+KW2h3vT9jGsUl2397a8BOI/dVECe8vzfiqcK1Dichx9OQwi0yCZNFYQMQa81vbw14ejuvp4dBxO2hT93N/WcYalHYzG1442afVuHisyjh48Mxj3Ryu/bGAcMgJu8N8Ls7QxoF/0WJ5u07Q14401oc688i9sc+nUIMPzmaMEvyKyUa3rrV52Inv+dJGHPleMpLp+qLY7eG/mKwnPP27QGtai48Yax59+6QF0/lfjiahhxOAgyVx+yDbDI1p+ZY3Bn4i8IG0hXa6/0prrkcw3L/++3tAVvN3Fd+nPDB/ognNvP72Wl6vHV7UPLfO3eHOKa5+DvOcuBSwQ9DP+LO0OdCqyyu88JmbsObtwacaVYXx2ZRwidHYy518nZ3hukKbJF37gywCzZsVW0uH08WhQ1AbxZxMA5LOTaL9KKwgTwHilpwaaPK27eHiwkBwM2Bv1i8gHRAHgXRorABCGLNe3eHpbw/nIYcTUIKIeS9/VFJn041PG5lK7xzRkHM7eGMhpvf47XejEnh/kwDetNoUdhApmMHY+pO3m5vHNAP4tIg8u7dITG5UXMde2Y3738XOhXeutWn4AY+OZqU/JLoNA9XdOx4wrlC7G8N/dL9Qapj3YLf5zr2UiEP5zq2W8vzdRomi8JmbsNbtwY8vrmkY/0Z7YJdN/ozgmRpHLg9oFPL7VzoWOFaB5NgJYbv7o0wjdyjsda8dXtAtzAODIOIW4MZdiEPrxxPF5O1uQ330rFnClp6N9Oxkv9uD6jYeV+LEs07dwZc6ub51J9F3B0FmAXjPzmaULyZeQ5s1PNYzHXs6c38Wi3P4Z1CYQNpu7qT2x7Gmt/vDfn22fbi2PE0HQcKQwq/3xthGLkNcaalT+3k/W8UxNzoz3h+O9fSqmMvChvIY9io5Xaea3m8vz8q+Xl/EnA8y/ME4Hd3hziF2MSJTucFlUIMMx3bLvS/T48mi8nu3IY3bw1w7TznfnCxw7t3hqXz7oz8ReGbXz9eFDYwz4EBTxf80JtF7I/K48CHB+OSJqd52Cv1v0k2lp9p5HG9OVg3DvTZLo3lmvf2hpwv5O+9dMyPcisarsntNTp2czDDNvOGV3uzFf+9datfmojfS8fmhcec390Z4lr5OXMd61bzPjnwU50+0yjHUBfuxTENDifl68917I/O53p0Z+SXxhjI+shoKYZ3hwwnM74qetNgUdhArmMTP/qMVl8Pvop3bv6vwL8JJOv+o1LqryulXlNKvba/v/8VmPPFCBO9MogCpYSGNAmKxQZA3w9pFSa9AGM/ZLOeH9NAsHStwSyiUUhCSAfl7aXHgrOldkGcYBnl0B7PQuoFG/woKU0uIBWy5Wv1ZyGqMFgADPyQllt+6OeHZd9Mw4Sly9ObRdSdcrslVxFrvVhNy9uFNJZ+b+hHbNdz0Vq2G9JJQHECAOmA2C0M+Mu/D2mszfIt05uGpYkqwDSIqBbio2GxIjVnMAtXbOhNQ04trXzMloRtFiVESfnY8SykXS23W/69RFMafCGNYXGAhHSAKhaa89+cs1GxVwbt9H4iakt9ctmHUaIJ4nJ/6M8imoXJuU5YifPc/tLv+RHVJduPpyHnO+XCZZkgTlgKIb1pVJr0QjppKnZvDfhxbkS35tKbrgp5bxZwrpUP3OtsmEUJYeF+6q5Ff41PizF0LINpuKozPT+isZQ7kzAuFZrLdpxpeRyvsf1oGrJRLetR0YaaYzFeo3Xr8nDsR5xv535Ic6DcdjCL8OzcTsswVnQTVvuRv07HpuHKtogo0aVYJ5rSJAeyHLDMlWOPbOT9aFm3IfWxWupIqYaU/bCs3XGiV/KwNwtpeOV20yhe0YflHBj6EVW73G4wW82L5XxKdaxsfG8a0ayU/ZduRyvr2LIN/VlYWhSCtAivLNmwnAezKCFc44etenkBZlkJEs3Ksf4swjKXx6KIpmeXji2HcRzGLI9Gx9OQ3cL4uxwrWNWxpmfTu0f+fl4MB35UmlBDOg6cXlqFXzYjiBPCgh4p1FoNmUYxO1nNarI6LwHo+xFVu2znKCjHfp0N0yjBWfJ7mof31hBIC8vVsXw1XpMoLhWD89+c0606a3WsPwvTre0FlvtfmGiWe9e6vuzHCWZhIFiXA4NZtNLueBpyobD4BiyeigK0PZv+bM34MQ1xl3Laj/KForpDaeE3tyEk1Msj28Nj3Zy3PwvXauXXjYda3Cil/nlgT2v9+r3O0Vr/Ha31y1rrl7e2th6mOX8lHNNgc2lCAKwIVsU2qFjlzrfbcLnRn5SOtTybW6O8IjaVwlsaKHYaLoeTspDt1F2uHU9Lx2pL7eqOuTJBOtVwuTPMK/6KbWIvFS22oVYGzN2Gix+Vk3Oj6nA0zW1XQHVJZNqevSIOO3WH42n5fqwlG1zLWJlMnGp43B6UVys6FZvrx/mx5ThAuu1jvLTCsNtwSytahoIlE6ja5krynmp4XO+VY9jw0vcdivfiLQ0UO3WXoV++5+26y8dHo9KxZfubrrUyYJ6quys2VJfaOaZamfDu1F2OJ37pWNO1S31EQalouT3y2amv7q3dqjkrA/xyDD3LwDVX+9Gtft5vtUrPK2IoVgqS7Vq5r0GaF+/cyp86Vh1zpV3NMVeKw1MNl+v9cu64llHqp5ahShO2m/0pu43VvN+quXx4kNuwrv+1PIvCAxIO7uHTot9n2Ttry+zWXQ4nZT80XKs0mBuqfK0P9kfsNlZ/b7fucWspn4rthrOIdmXVhlONVRvaFZvLvdynplIrfXKn7tKb5e0mYVx6CrVouzQaNRxrrY5dW8oBxzBK0xfbUFhqVYN7SzmwWXN5PdvuA6wU7ZDq2HLhcqrhcmtQvtbyJN+1jJVjp5oet/plv9cdszQpNBQr+rdVczheyoHNmsNgSduWC8Gqba4UmrsNlxvHZe1puGZpIpXmc1m8d7L3rYp0KjajpSefy2NR07XwlgK723D59Dh/0mqZakVDHNMoPYVM2zkMl7SnW3E4LoyRilU971Rs1NJYtNtweW8/94NrGivtPMsoTfxvD6Zrt+NUbaNUHJlrdGyn7pSehEKqYx/ul/vysh/qjllaGJiG0dqcrjsW2Q5IYqDurvblnbrLwVL+dio24zCPoWI1D1uetTLJPdVwF1u95iznvWuuGcvr5XkIpHm+nANFPb01mK0fi6oug6X+sJzDVdtcmYfsNtJ3cZfPKz45ThcFlnJgjf7t1F1+e/u4dKxSiNfBxF8pAiH139GS7VXbWjwBGAWsLATPbXDM1UXBh8W6cWC36VH7ql5o+SvwsJ/cfB/4F5RSV4D/N/CnSqn/50P+zYdCy7P5xqnmYlC2DJW+o2KoxapD1TZ55WyHw8lsIW7bNYeLnSqT7DGroeCprRp121wkgWsavHquzTTIH/O3PZtntxuLx64KuNip0q3YWNmk0DIUL51pYaEX583fizCNXGBPNVzOtCpcz94/MBRM/ZBXz3UWE0zPMnj1XIexHy5EvluxeXKrzkeH04UNj2b7gueroLapeOVsG0NFC2FuuBbfOt3iVm+6sOFs9n7NfOXIVIpv7jZpetZiMl6xDV4922Yc5DZs1hwe2agutl8ZKt0X3PTMxdMIxzRwzDQecxta2X7i4mPd822Praq9iJdlKCpWav98ZWr+bpCl1ML2nbrL+XaFaSGGT2/Vqdkmlcx/rpXGcOwHi6c+7YrNM9sNbmQTGgVc6lbpuDaWkflvHkMjWRSbdcfkxTMtrh9NFjacbricbnrczgpiU6V7u2umWjyBmcdwOMv9t1G1eWKzzp1RuLDhsY0qG1V7MRjZpuKVc22SKI+haxpsVm0utCsLG+bv18wLYDPLgZZnlXLg1XNtDifThQ1bNYdLnQrj7OmUoWAchLx6rr24lmMafPtcB9disYLW8iye220uBlYFXGxX2KjYzIcFy1DoOOKVc+1SDrx8ts0wCBe279ZdzrYqixVBQ6XvN7Q9q5QD3z7XIQijRQyVUpxppvc9t2G+N95QeQwtI+GlM61SDL91usXtgzyG4yDhmZ3GYkuTqRTP7zSoWnkMK5ZBzTZ5eqteiKHDYxu1xTkKeHyjxkbNWkygHdPglbNtSMJFDBMNm1Wb8+18Qnau5bFVsxfbSi1D8cLpJhUz1zHPNmm4Fk9s1PIcqDlcaFcXxftcx2qWketYlgPRso7tNNgv9L/hLOTF0+3FU6C5jjUcq+S/l8+2ShPFUw2XM01vsTJqZDnQWorhq+c7zKKkrGObtUXuKODRjSpt18Qs5ICtNS+eaS3pWJP9kV/SsZ26uzjHVIpv7DZwTKOkY98+2+aokAObNYdHOpVFX57r2EbVKeXAq+faeKYq5cDzu43SpPd822OnnrezDMWLp5vpBwqKOnY2vZdlHesHqzrmFXTs2+faOIZa5EAn07FJmOfhI50qW9VcC2xD8fKZFppVHbtxuKRjDXfxDp2p0hX/b59rl3TsO+dTG4o69vhGnWvZGJbqWI2Wa1Jx5v5TfPtcm6plLPzVdC1eON0sbRk91/LYrjn0sjHFNBRRHPPqufaKjh3P8hhGGh7pVNjKJqvzHOgWYpiO5R1cs6xjz+40F0+d5jrWrdiobAY2z4G6Y5Z07KWzbe4WxoGPD6c8sVlfbI8yVPqeUc1WpRyoWYrndhqlGD69VVsUWPOxfKtml2N4tkXVzv3XcCxePN3GKuThmabHTsNbvO9lKsXzuw28wlhUsQ1eOddmEkQlHXt0o0aUNZzrWLe6qmNOQccc02CzVtax822P3YazaDfXMSs7fx7Dl7P5RFnHKiUde3qrRqdil8byb59r45qqpGPPbDewjVyDL3Yq2bZZa+G/l860MBSLHPAsk7Zn8Wi3WtKx002PDw7yd/ue3WngWUsxtBXP7DRKOvbEZo2699W979JyLZ7aqpXG8kc6VRxntWD7uqG0/mqqQKXUPwP8Lz/ra2kvv/yyfu21174Se74ovUnAJIqxDYOmDa6bfokqiBI8x6RbcZiEISM/IdGamm3S8GwGfsjYjzENRd01qNo2R+OAWZRuD9qoufi+zyBMH6VWHYO25zAKAkZ+usWmblvUPIvjacg0TLdcbWVbNA7GPkGcfqWkXXGYhiEDP0brdGWp6TlMgpBRZkOnYmMYBkeT1AbPMulWHYIgoBekW8OqtkmrYjOYBUzCBKWg6ZpUbHvRLhWe1Ib9sU8YJ9Rsi1bFZjyLGGWrQjXXoO449GYBkyAdAFf8Z5l0a6ntQz8hTjQ116Tp2gxnIeMw/cpLyzVwbZvBLFx8oaZdcQr+S6haJu2qw8iPGAfzF+KtdGvQNGAcpjFsuwa2bXM49vGj9CslnarLLAzpZ/6bx3A4DRmF6Vde2q7CcRwOJwF+WI5hP0y3NNSd1O+jWcAoTDBIV2fqhRgW/TePYcWy6FRtRrOISRSRaKjbBnXPoT9N79k0FG0nsyGz3bVNNuYx9DWxzmM4nAWMl2J4PEn3+TrWqg3zfjQe+4wSDVpTtQwaVZf+ZMY40uUcGKXtPEvRrXlMphNGkUGStWtWXQYTn0mUYBiKuplQrVQ5Gs+YRTr1Q90txbBmKVpVj2HWDqWoG4pazaU39pnEaT+ab3E5GM0IYo1nGXRrLtPZlEGo0FpTMxWNmkc/u5alFC03wnHqHI58/DhZxDD1X/qFn6pp0Kq5DCYzJpHGUIqqDXXPy/1nKjYzG/aH6b7veT8aTWeMI9KvpdkG9Yq70BBLKVqOwnXdPIamYqPuMZ6OGcdmmgO2QbPiMsz8bihFw9JUKhWOxz7TQrvZbMYwUmkOmIp2zWM08RlnE4qaqahXXXrZ/ZRjmPqvYhl0ai6TyYRRnMawZikaVY/B1Gccpls4amZMrVJbxLCkY4Em1DrPw2nAKIzTr31ZUKvk/rPNQgzHM4JIU7UN2lWX4XTKJEpjWLUUzapHP4t9modGOQdMg426SxBM6fmqHMPxjEmcfg2qmfnvaOwzixIcS7GZvSOzP0pjWDUN2jWX8XjGKAEyPa9XHHpZP7KVopnFcG0OxAZJkudAfzJjmsWwbiZUq9Xchs/LgeUYLnLAoGFpPC/9GpZfiOF0OmWQ+W8ew94k7TOp/2Icp7ZoV9KxQBNpTd0yaVYdRlM/1TGlqFpQr6zPgUU/mufAbMYkhKSQA/cXwzE93yTW6f20qy7D8YzxUgznOVC2wSdIkjyGU59RtjhVtRSNyoPrWCWLxYPrmEGr6n5xHSvGcK5jWbsvQ8d6E5/J5+jYeDpjtNCxeQ7cW8cqlqJTy3QsSmP4hXXMUrSrn69j8xx4IB1TipqV6tjxOM3NL0XHMhu+qI7NYx8EU/q+IirE8KtmMZ9NNNVsPvZ1Qin1utb65ZXjUtwIgiAIgiAIgvBPE/cqbr6ynXNa678E/vKr+j1BEARBEARBEP7/i6/ia2mCIAiCIAiCIAgPHSluBEEQBEEQBEE4EUhxIwiCIAiCIAjCiUCKG0EQBEEQBEEQTgRS3AiCIAiCIAiCcCKQ4kYQBEEQBEEQhBOBFDeCIAiCIAiCIJwIpLgRBEEQBEEQBOFEIMWNIAiCIAiCIAgnAiluBEEQBEEQBEE4EUhxIwiCIAiCIAjCiUCKG0EQBEEQBEEQTgRS3AiCIAiCIAiCcCKQ4kYQBEEQBEEQhBOBFDeCIAiCIAiCIJwIpLgRBEEQBEEQBOFEIMWNIAiCIAiCIAgnAiluBEEQBEEQBEE4EUhxIwiCIAiCIAjCiUCKG0EQBEEQBEEQTgRS3AiCIAiCIAiCcCK47+JGKdV9mIYIgiAIgiAIgiD8VXiQJze/Ukr9p0qp/6ZSSj00iwRBEARBEARBEL4AD1LcPAH8HeC/B3yslPrfKqWeeDhmCYIgCIIgCIIgPBj3XdzolD/XWv93gH8V+B8Av1ZK/Ugp9d2HZqEgCIIgCIIgCMJ9YN3viUqpDeC/S/rk5i7wPwX+c+AF4D8FLj0E+wRBEARBEARBEO6L+y5ugF8A/zHw39Za3ygcf00p9e99uWYJgiAIgiAIgiA8GA9S3Dyptdbr/oPW+t/5kuwRBEEQBEEQBEH4QjxIcbOplPo3gWcBb35Qa/2nX7pVgiAIgiAIgiAID8iDfC3t7wPvk75b878GrgC/eQg2CYIgCIIgCIIgPDAPUtxsaK3/fSDUWv9Ia/2vAN95SHYJgiAIgiAIgiA8EA+yLS3M/v9tpdQ/B9wCzn75JgmCIAiCIAiCIDw4D1Lc/NtKqRbwvwD+XaAJ/BsPxSpBEARBEARBEIQH5L6LG631f5H9zz7wJw/HHEEQBEEQBEEQhC/G5xY3Sql/F1j7CWgArfX/7Eu1SBAEQRAEQRAE4QtwPx8UeA14nfTzzy8CH2X/9wIQPzTLBEEQBEEQBEEQHoDPfXKjtf6PAJRS/xLwJ1rrMPv73wP+7KFaJwiCIAiCIAiCcJ88yKegTwONwt/17JggCIIgCIIgCMIfnAf5Wtr/HnhTKfVPsr//GPibX7pFgiAIgiAIgiAIX4AH+Vra31NK/QPg29mhv6G1vjP/70qpZ7XW737ZBgqCIAiCIAiCINwPD/LkhqyY+f/e4z//x6QfHFiglPKAHwNu9lv/mdb63/oCdv5BCOOEKNG4loGhFAC9aYDWik7VBiAIAkYR2ErRqKTHRkFAGIFjGtTc1MWDWUCcaDpVd3H944mPYShanpO2m0WESYJtQD07NvBDokhTt8Fx0mPH0/TfU+1UCjaEYFmKppseG0wDQg0128CzUxv6s4BkjQ2moWhmvzf2I4I4wbYM6k7WbhoSa03N1Lium7ULUUrTrqTtJmHILNDYpqLhpTYMZwFhDBVHUbHthf/Q0K6m7XzfZxwrTKVoZfczDSNmYULVNnFtM7cBTc0o2hBgAK3sWkEYM4liXNOgktk+8kPCWFN3DGzLymOIWvWfoWjObQhCZpGmYhl4zmf7TxmK9tx/s4ggSbAtqDv3jmFvGgK5/+Y2mKailflvNAsIE6jYCi/zX38SEKPpZjaEYcgw0pjk/pv4EdM4wTENGm45hnWrYMMkAMXChmkYMl2O4WRGqMEzEqqVatpu7KMVCz/4vs840mkMs2PDiU+QaDylqNXSY4NJQKw1nVruv6Oxj6k0raqX2jCdMksUpoJmdmww8Ym0pm7HOE5trQ2p/xIspWhmx0ZTnzDR2CbUPS/zn0+iKdlwPPYxlaKZ9aPxdEaQgG0Y1DPfDLNr1W0jz8OJj9LQzq41mU6YJQa2gkZm+3A8IwQqhqZSqWR+n5FoRbdW9B+YQCs7Npr4+InGNRT17H76Y58YqFkscuBo7GMoTbvgv2misIFGzbvvGM79ZxuKRmXuv4AwSXAMqFXmsViN4fHYx1AsYj+azQhjsA1FvTKP/WoMl/0XBGNGoVmK4WAyI9bgFfzXn8yIC/5bG8Oxz0xrHEPRmPtv4qc6ZqmChnzBGI5noBTt5RxALWI4z4GKoah+TgyXc2CaKKxCDvQzP9xXDhiK5nIMTahlOdCbBOg1MVRKLXR5XQ4Mpj7R5+RAGE4YBmX/DSYzIl3233IM1+XAZOIzTZZiOPbTcaAQw97EB61p15ZyoBjDh6xjx1kezmM4m82Yxnyujh2PfSjFcDUHRMceXMfW5kBBx+6VA5+rY2tyoD+ZgYZWZueXqmNTn1msccxcl79qhtmcsGIaVN0HKhn+oHyZlqo1x3zgT7XWI6WUDfxUKfUPtNa//BJ/96GwP/Z5+/aA/izifNvjUqfK0TTkg/0RiYbHN2ts1xyuHE+51p9SsU2e22lQNRVv3x1xNA3ZrDk8s1VnHMa8e3dIECdc6lQ50/K4PfT55HCMbRo8s12n5Vi8dzDi7iig7Vk8s9NAJZq37g6ZBDFnWx4Xu5qjScCH+2MAntiqsVl1+ORowo3+jLpj8uxOA9uA390d0ZtF7NQdntisMwoifr83IowTHt2ocbrucn0w48rxBNcyeGa7Qd0xeXdvxMHYp1txeHqnThhpfrc3ZBrGnG9VuNCBvVHAx4djDAVPbtXpejYfHU24NZjRcK2FDb+9PWTgR5xquDy+WaM3C3l/b0SsNY9t1NipuVzrT7nam1KxDJ7ZaVIzFb/bH3E4CdisOjy93WASxvx+b8gsSrjUqXC2BXcy/1mGwdPbdRquxUeHI+4MA1peagNa8/bdISM/5kzL49FuHkOt4YnN1H9XehOu92ZUM/+5huJ3e0OOpxHbdYcnN+uMw4jf3x0RxAmPdKucaXrcHMz49GiCY6Y21B2LDw5G7I0COhWLp7cbJInmnSyG59oeFzuag3HAhwdjVMF/nxxPuNmfUXfTflQzFa/dHtKfRew2HJ7YqDMIIt7bGxFlMdxtuNzoT7lyPMW1DJ7daVCzTd69O+RgErBRdXh6u44fad69O2AaJVxoVTjf1uyN8xg+tV2n5dp8cjjm1tCn6Vo8t9tAa83v7o4Y+hGnmy6Pdg16s2iRA49tVNmuu1w7nnK1P6VimTy3U6diGryzN+JomsbwqW3NNEz4/d4QP0q42KlwrulxexSkMTQNnt6KabgmHx5MuDvKYrgNidb87u6QURBztulxqWtxNE39h85yoGLz6fGUG/00hs9l/e/duyOOZ/MYwiiIeW8vj+HphsvNgc/l4zSGz+zU6bgW7+yN2RsFdCs2T2/XSWLN23vzGFa41NbsTQI+ymL41FadDc/io6MZNwc+Ddfk2R2NZSjeuZPH8PFNg8Es4v29EZFOeKxbY7fucG0w48rxFC+LYdUyeHcvzYE0hppZlPDu3TQHLrQrnGvpNA+PxphK8fR2g45n8v7BlDtDn6Zn8Y1diBLNu58Rw8c3q2xVXa72Uh2r2ibPbjdwTcW7e6mObdUcntxSaR4WdazpLmI417G6Y/LhwbikY8UcONvyuNgxOZqGqY6pPA8/PQq40Z9Ry/LQU5q39sb0FzqmGGYxzHXMyXRsutCxim3w/t6Yg0mmY9uaME743d4o17E27I19Pj6cFHQsjeGtgZ/pmMYy4O3bo4WOPbah6M8i3s/89+hGlZ26y7VeUcca1EyjpGNPLcXwUqfC2abmzjwHDIOnt2OarsWHh5OCjoGRaN7ay3Ss6fFI1+J4GvLBQVHHbK70pp+pY09swiSI+X0hB840PG4Ocx17ZrtOwzF572C80LFnthtESZqHkyDmbNvjUjvhYBLmOrZZp1ux+eTI5+Yg07FtTdVSvF7QsSc3DPp+pmNJpmN1hxuDGZcLOVC3DH63N8p1bEszixN+f3eY6li7wvkW3B37fJLF8KmtOhtVi/f3p9zOdOzZHY0J/LaQA491DY6XdGyrlsZwMZZv17FNg/cWOuby1DZMs7FoWcc+znLg6e2YxkoOgM5yYBykY9EjXYvDSVnHtio2nxwHZR1T8O5eqmM7WQxHWQznOXCq7izpWDqWv7c3Zn+c61gUp2P5ZJEDmv2Jz0cH98qBVMfMTMcGs4jdhrtWx7brDtf7M6728hhWLIPfF3Ts2W3NpJADFzsVzmc58PHRGEsZPLUd0/QsPsp0bJ4DOhsHhn7MmabLI5mOvV8Yy7eqDpd7U673pmkObDeomCobi1Ide2pLlcbyuY7dGgV8ejhejOUtx+T38xzwLJ7dqRMm5DnQ8rjUSThc0rFuxeHyUcCNQWE+pjTvLOuYH/Pe/mfrWNUxeO9uWcd2Gt5XOg/eG814b6+oYw2263+YIutBUVrf85+webALKfWG1vrFz/jvVeCnwP9Ya/2rdee8/PLL+rXXXvtS7Pmr0J+F/NlH+8RJ6hsTeOV8h19eOy6d99KZFlcPhxzMEiCt7v7oUpcfXT5anNN0LTaqDpePJ4tjz2zXCaKEj4/yY9+/0OVnV/N2rmnw/Ytd/uKTg8Wx822P03WXX97oL469erbNmzd6hNnfhoLvni9fq1uxefF0i39cuNY3dhvcGc7YG4eLYz+42OWnV/J2Fdvg+xe6/OOP83aPdqu4puL3WYEF8N3zHX5R8I1lKL5/oVPyw07N4YXTDf7RR4cAPNGtoJXBR4f5ddb571unm7x1a1D6h5ae2qpzvT9lHKRfIn9uu8Htkc/hJFicYxuKV862+XnBrrNNDz9O2B/n5718psXv7vaZRUX/dfjZ1bzdi6ebvHFrQJFndxp8cjhmFiX3PM+1DL51ulXqNxfbFdqeyVt3Rotjr55r89r1HvMrmQr+6NIG/+TTw8U5379Qtgngm7tN7gyn3M1iqIDvL8Wwapt851ybvyhc6/HNGneGPkM/vemnt+scTQLujnK/PLfT4P39EVGSe/5UwyXRcHfkF+65xe+yCe/chh9c6vKTQgwbrsULpxr85Epu/1NbdZq2wa8zfz2/2+Bmf8bRNO+Pjql4dKPGe3u5r861PJquxbuFYy+ebvHW7T5zUw0Fz+80+e2dPBbdik3dtbjWmy6OPb/T4MPDMX4hhj+82OUnBf95lsEPL3T58yx3KhY8s9Pi9Zt5DgJ8+1yb3xRjaCie2a7zzp3h4pztuoNlGNwazBbHvnmqye/vDgkz4xXwvaVY1xyTUw2Pjwu58sRmjeNJwP4k99f3zndK/f37Fzr88npvoWOQxvC5nQZ/nuX08zs1RoEu6dM6G5quxaMbNd68ld/3M9t1TAXv3B0t7uVab7p4sgypjj3SrfLefh6vC+0KQz8qxfrF0y3evNVf5LmR5cBfFvptt2Lz3E6DHxfis6xj/43HN/nFtd6ib0OqYz+40F3cc922eHK7thLD75xr88vrvcXfa3Ws7nCuVeG1QttvnW7y3t5ooQXrdKzumHznXKekwU9t1bnemzIO839R4cUzLd4oXNs2FT+8sMFffJq3O9PyuNiulOLzrdNNfnt7UMqBZR1reRZtz+ZqIQfW6dgPLnT5aXEssgwudaq8X4jhpU6V3iwsxfrb59p8eL3H/BfX6dj3LnT4+bKOnWpy5WhM348X/vvBUh5WbZPvnG/zF58UdGyjxsAPS7q1biz64cVuyYbduss3dhv8WWFce+lMi8sHY46yfvPtc23evjNgGuZ+abgW3z3f5s8+yts9vVXHyAoQSPvjjRUdM3h0KQfOtyuMg7g0Zr1yts2bt3rMQ/FAOnYwxo+LY1GLNwq56lkG59uVtJjKeLRb5WAS0J/lufJS1v/mebhOx7ZqDts1p6TBL5xq8v5+OQeWNeR7Fzr84upxaSx/YrNGxdD8di/Vn2e3G+yN/dIYbRuKJzZrpd8703QJ43SRbs63Trd4+3afuJADP7jY5ceFPGx5Fp2Kw5WC3j2706Biwmu38ntczoHvX0j7VUFKOd+u8PxOlf/yg7Rv/TOXunycLTTPWTcf26jaVGyzdN43dpt8ejRmFORa8K1ME+dU7HQsKj7peZgcTQJ+euWISUGf6o7J9y90SrtX/tAopV7XWr+8fPxBvpb2RX/YVEq9BewBf36vwubrxGAWliYE/61ntrnZn66cd6035dXz3cXfGhgUBlWyv6uOWTp25XjKxU61dOxg7LPbcBZ/+3HCOChf63pvRi3bLrSwoT/l1Yudxd+JTleXihxNw8Xks2jD01uN0rHeNKRi5bZOw1UbrhxPOdWslI7dHEx5rJvfT5ToUkIA3B0H+IVD5zq1ksBA6r+i0BoKZlGy8i/IXj6acKqwgtHwrNIgARAmeuWebwxmbC0Jw7XelBd2W4u/E03JdttMV4uXuXI8YbdRvtbQj3HMPKX8KCn1I4CrvSndWnn15WZ/xtl27tNYU5qcPbFRKxUUCxt6E57daS7+Tv0XUuxukzAuTVxg7r/c9o5nlyYI82tFS7bfHvpsVp3Ssau9KZc6lVK70VIODP1oMeAsbD+eLLYTAtQdqzQhAAhivdgOOudGf8bm0srRzcGMTiW/VqIhWlq0OZqGiy16uQ1TdpaudTQJSr6ZRQmjML+fb51qlSYWCxv6M04187jGiWbJfdlKeDl/r/ambBVs0MAoiErCPA5iXKss1VeOJ1zq1krHbg99vnMu78uzNf3v9tAvHduuV7jaW83D5fwd+BGOWY5FqgX5PVdsozTZhVTHDKPc7lpvupI7t4ezkm8SvdqPlvvH3Iant3MdmwRxKXcg1bHipOEbp+pcOV6N4a3hrBT7tTo2Clb0/OrxlEcK+rduHBgFMdOofK3LxxN2m2U/HE9CqnZ+/TDWjJY0+GZ/ttIfbg5mbFTLObBse38WLbYaz7lyPFnJgcNJQNvLbfCjBNNYjv2q/t3oz/jTZ7YXfy/r2PPb9fU6djzhqUIM5zrmFUydhDGzcHkMm6yMo7eHM/7Zx7cWf0eJXhnD7oz8xWJCfq0pL57Nc0drSoUNpPcyCVZjeLqQA9W1OraaA9d7U3bqzsqx84Vx4IF0bCkWoyDCKvzmLEqwzXKfuXxcHkchXbhqFhy/Tsf2xwFNb1XHHl3KgVEQL3TMAMZBtDKWXzmestXI2zU9q1TYQDqWszQO3Bz4bNaW+990JQdG/moO1Jby9/LRhI2lax1MfHYL8ZmEyYofrvem+HFul2kobhYKlrkNy/Oxw0m42Ho+J9Xzcl+ehjFFyV3WsYfNyI9WNGQUxItF5a87X2ZxE6w7qLWOtdYvAGeBV5VSzxX/u1LqryulXlNKvba/v/8lmvPFsYyyW8Z+VJr0z/Esg9lS8Jfbrtur51oGyVKmuJbJOCiLqb0kiI5prFyvapkMp2XxXhZSQ7EyOLmWQZAs/Z6pCKLPvh/XMkiWBLdimSsTCkOV25kqfa9mTqL1ygCd/l5+jtasTG7nNvhLhYuxxtHLfrANtTLZ82yztHI6t3VhZ6JLNi1sMI3Sij+AZa5e31Srfkcv22CsiEjxN3vTAG9N/3Mtg2g5hoZBvKQ9y7H3LIOgUG0kWq+cs67fWoYiXrbdMlbEe7nPLN/PvN3SXHltDJcP2eYa/1nGSiG73E4ByyOru6adbRqMg/IEzCzczyiI8Nb024ptrvhh2QZTsZI7nmUQLPUj0zAoH1m9lmuZK7Z7tsFxochf7nuQ5kAxPFprXHP1fpbzTq05lvbl4jlqbb9ZPuZYxsrkcl0slvukoVZzermdteZeoNz/JveIoWetxtBc1rE1ndSzDCZhWf+sNb5f0VKznIeQanC4lNPLuWObq552LXNFj5bjf6+xaNnvzpqcXu1/BuGS7RXbYBbf2/aje+iYZ5nM1ow7Sy5dO4aFS79XsQyOJvfO37lNy2FMx/Ko0Gadt1b7l2eZJVlJ82S13TodW148qtgGk/AL6Ji9qiGWoVa0Zn0My+1cczWuqzqmVoxIx4E1NmT/O2E1DnMblMqvpdEr48I6G+w1Y9G6vrycO/fKgRWNMk1Gfn6tdVrqWEZpAq2Uwl5j/DodW94x5VkG/lIOmIZaKajWzUUeFvfU0nsc/7px31Yqpf7W0t+mUurvz//WWn/ns9prrXvAXwL/7NLxv6O1fllr/fLW1ta6pl857YrFVi2v2v/8kyNON71SsWEquNSt8ReX88euDdei6ZbF+/HNGofjXGwV8PR2g5/dyB+Te5bBZs0uFQinGu7KQP7sboOPD/JHs5ahONeu8Pbd/HFq27NwlqL6xGaNqZ9PehTp/tpfX+stjlVtk7ZnU0yvcy1vRaif223w9u3CtglDcarpcrew2tKt2rhLSf70dp3pLPfDGzf76XsxBeqOSbOwKqUzu2p22afP7jS4M8hXXq8dj3lqq146Z7vmrBSQz+02uVloZyrFxU5lsa0G0u03xaIr1tByrdJkaB7Du8P8fjzLoOVaJcE93XRXVmuf22nw+7v5NgPLUJxtVjgo+K9dsakX+tHeJH1/qzgJNbJ97j8ubPWq2iZNzyrF8ELbI1karJ7baXCr4IcrR2OeWfKf1rBZK68uPbvT4FbhCaah4JFulWuF1aqGY62sjD3ardKflvvf09sNfnU9395xoz/hyc2yDacb7spg9exOnQ8KWyLNLAeKudP2rJVB5smtOnuj3E5F+q7RXiGGFcugW7UZFOZGZ1seFTu/1tt3xzzSrZUGYNtQnG56pRXbbsVeXmzk6e0GdwblLQuPbdQ4KBQkNWe1vz/STbcALfvh/cI2Dcc02Km5fHBYjI+iu/Sk6JmdBoOCne/c6fPcbrN0TsO1qCxN/h/bqLG/5L9nthv85Goew9v9KU9slZ8mnW54K4P28zuN0paMeQ4UVyXbnkVjqR89sVnjcMmGZR0zobSCDKmOVQuL3W/dGfFot1rSNttQ7DZceoUnx92qvfK06umtOlcL2wPnMbxynNtVd0waXnl1/ZFulXilL5d1zDUNNqtOaXK5U3NKT4Pn7a4VnraZSnGhXSk9LWouaRak73Xsj8v+e3qrvqJj3Ypdesp+tuWtLL48v9ss7WawDMXZVoX/8oO8P3SWdOzmMGBrjY49sVnjt7fzMaxmm7Qr9pKOVYiXdOzZnUZpq5djKnYbHr++mevrZtVZWUR7ZruefhCiYMOjGzV+ei0f14aziPOt8lONR7tV3MKlFPDMTp1fXSvr2BNLOnaq4a4sGj6/2+BmQQvmOnanEIu2Z61MZtfq2FadvcITsYqdfkimOPyda1VWngA+v1OOoW0odpvlWG9Uy/oB6Vh+tbClfp4DnxZ2YtQcs/QEEtK4Lo8Nz+7Uef16PoZdOyo/xYN0O2+0HPvdBrf7xbEcLnaqpfxtutbKU9bHN2scjsrzsWe2G/zkSh5DzzLYqNqlJ/aupWgt5fRzOw0GBV2+PZiuzGnano29NB97eqtReoKpgCe26nxykPuvapvUnXLhfK7lUV9dG3ho1GyDC+1yDjzSrVJ1/un4qMB9v3OjlPoPgQ+01v87pZQL/KfAG1rrv/kZbbaAUGvdU0pVgD8D/h2t9X+x7vyvyzs3kD5CPZyETMOItmfTrTocTUKOpwGaVLgblsmRH2ZbNgw6no1CMQhCxkFM3bVouCZJkn7hLEo0bc+m6SmGfsLxNH103K5YWIbJ0A8Z+hFV26TlWWigN4uYRTEt16LpWUzDhONpiCKdBNds6M0S+n6EZ5m0PQsUDKbpI8WGa9FwbaIkpjeNiBJNp2LRcA0Gs4TebG6DjaVgEMSM/PTRbcO10Wh62ba2lmfTsmEcq4UNnYqDa6btBrOISlYkaTT9WcQ0TF8QrLsWUaw5noQkWtOu2tRNGISa3izEMY10UmoYHM9S/9Uck27FJojTc8JYZ/vGDQaZ/0xD0fEsKrbJ8TSNRTUbHBOtU/+FMS3PpuOZjMKE3jRciWHfj/DM1O+mAb3Mf3XXou2ZBHG6bS9KNO3Mf0M/oTfN/WcbMPDjRQybnoXW6aPwWRzTdm3qns0siDiezf1n4xmKfpj6z7OzGOp0a8s8hi3XIkjSe46zGDYdRc9P/WxnNpgKBkHEyE/91/QyP2QxbHs2TRtGsaI3CVEKOlUH21SM/GgRw5Zno3RCz4/TGLoWTQt80q1HWkOnYlG1NINApdvhLIO2a6FUukVvHMZZwWoSJWlfjpKsH5kxwySNmanSL9eZCkZhzNCPU/+5Zuo/P2IWJbQ8i5ZtMo01x7Mshp5N3YBelPYRz0r7kdKKfjD3n0nDMomA3qyQh07MIDDpzUIsw6DjWRgKhmHMKLOh5ZqFPEz917FhmMDxJEr9V7HxlKYf6TyG2aRu4MeLGDZtRaAVvWlIXPDfKFRpDhgG7YqNoROG2RaEumPSsA0SZaQxTFIb6rZmEqk0B1SqBY7SDELN0M9imNnQ82NmnxHDmgn9kEUMO56FymwfhzF116RhmyQajrMYzv03DEyOZ2GaA56NBQyjPIYtx0IrvfBfy7NoWgbThDwHPJuKCf1QZ9uR0hiW/ZfaEOlUS2OtaVdsmkbMIM5jmE4I03ajIKZmmzSyftTzI4J5PzJhrFP/zWPokjCI0ryrZDHUGvpBngN1WxHpVP8SnS6EVS3NKFD0/HkMLQxSTZzrWMMx0FrRy76I2fJs2lbCIDYWMexUbGxDMwh0riGuARj0/FTHmp5F0zaYJakepTG0qRrQjxL6swh3kQOpDZMshi3bJKSgY55Nw4kYBlbmv0zHgH4hB5qOiVZpDviZ/9qWwTgb11TW/yom9IOkkAMWkDDwk1zHHIMgmccw7X9NM6EXGfRnIXaWA4qEYZAs/Nd0TBJSXQ6SJNVSJ82B3jTCyPxnKc0o1IsYthwTpfhcHaspTT9Otfp+dazt2TSLOmYoOl46jg6XdIyChqTjqGIas6Jjx1kM71fHOp5N43N0rDbXUtL8DaLiWE4pBzwS+lkOFHWsn/lvrmNhlgMPW8dKGjzXMc+iaSn8zAatoVO1Uv+Fuuy/zPbJQscsEq1XdCz33/3pWNuzaVhqjY6lY3lugw3oko7VbZP4C+rYZv2r/aDA4SRgMJvPZ02ajvWVvfNzv9zrnZsHKW4U8PeBd4A/Af6B1vr/8jltvgH8R6QLagbwn2it/9a9zv86FTeCIAiCIAiCIHw9uVdx87nPl5RSxS+g/W3g/w78DPiRUupFrfUb92qrtX4b+NYXsFcQBEEQBEEQBOGBuJ/Nc/+npb+PgWey4xr40y/bKEEQBEEQBEEQhAflc4sbrfWffBWGCIIgCIIgCIIg/FV4kK+l7Sil/n2l1D/I/n5GKfU/fHimCYIgCIIgCIIg3D8P8sHq/xD4R8Dp7O8PgX/9S7ZHEARBEARBEAThC/Egxc2m1vo/If33mNBaR0D82U0EQRAEQRAEQRC+Gh6kuBkrpTbI/mlapdR3gP5nNxEEQRAEQRAEQfhqeJB/avR/DvznwKNKqZ8BW8C/+FCsEgRBEARBEARBeEDuu7jRWr+hlPpj4ElAAR9orcOHZpkgCIIgCIIgCMID8CBfS6sCfwP417XWvwMuKqX++YdmmSAIgiAIgiAIwgPwIO/c/D0gAL6b/X0D+Le/dIsEQRAEQRAEQRC+AA9S3Dyqtf4/ACGA1npKuj1NEARBEARBEAThD86DFDeBUqpC/rW0RwH/oVglCIIgCIIgCILwgDzI19L+LeAfAueUUn8f+D7wLz0MowRBEARBEARBEB6UBylu/vvAfwn8Z8CnwL+mtT54KFYJgiAIgiAIgiA8IA9S3Pw94AfAfx14BHhLKfVjrfXffiiWCYIgCIIgCIIgPAAP8u/c/IVS6kfAK8CfAP8j4FlAihtBEARBEARBEP7g3Hdxo5T6r4Aa8AvgJ8ArWuu9h2WYIAiCIAiCIAjCg/AgX0t7m/TfuXkO+AbwXPb1NEEQBEEQBEEQhD84D7It7d8AUErVgX+Z9B2cXcB9OKYJgiAIgiAIgiDcPw+yLe1/AvwQeAm4CvwHpNvTBEEQBEEQBEEQ/uA8yNfSKsD/GXhdax09JHsEQRAEQRAEQRC+EA+yLe3/+DANEQRBEARBEARB+KvwIB8UEARBEARBEARB+NoixY0gCIIgCIIgCCcCKW4EQRAEQRAEQTgRSHEjCIIgCIIgCMKJQIobQRAEQRAEQRBOBFLcCIIgCIIgCIJwIpDiRhAEQRAEQRCEE4EUN4IgCIIgCIIgnAikuBEEQRAEQRAE4UQgxY0gCIIgCIIgCCcCKW4EQRAEQRAEQTgRSHEjCIIgCIIgCMKJQIobQRAEQRAEQRBOBFLcCIIgCIIgCIJwIpDiRhAEQRAEQRCEE4EUN4IgCIIgCIIgnAikuBEEQRAEQRAE4UQgxY0gCIIgCIIgCCcCKW4EQRAEQRAEQTgRWA/z4kqpc8D/A9gFEuDvaK3/9sP8zS8DP4w4mISM/AjXMuhUHcI4YehH+FFCzTFp2CaBhsEsJNbQ8iyarkFvFjP0IyzDoOVZKAUjP2YaxlRs8//X3p8HS5Jl95nYd32PPd6W7+V7+fJlVmbte1VWdy0NkARIkYKBDQ4HpKFFGwIiJdgIpDSkaWjGIW2koaixgUSabIYGg1EQwW0MJEcQOAQpkpCBAJq9VHdVZXVtXVvXluvL7a2xh29Xf7hHhLtHZFVWZ2ZV1uvzmaVVxs3w68fPued37/HrHkXdNQljaA1Dwjim7lpUXYOur9kfhJgKGp6NZUDHj+j6Ea5lUHdt0Jr9YYgfxVRdi6pr44ch+4MQrZPjao7B3iCk7YfYhkHdtXBtg91eQD+IKDsmC2WHXhCxNwiJ4pi6Z9O0NPuhSmwwFA3XwjIV7WFIz4/wbJOaYwKK/UGAH8XUXIuqbTGIY/b7AQqoexZly6Tlh7SHIY5pUPcsDBT7w2Dsv4ZnMQg1rUFIpHXiPzNmP1S0Mv4zlEF7GIz9V3NMYmB/kPiv5lo0PJPOMGZ/EGKk/nMtzf4gnvjPs0Anfh/ZUPcMhqGiNQiI0xhWXYP9QgwNoO1PYlhzbWIdj22ouxYNS9OKjDSGirpn4RjJcdkYapJrHvmv7lj0wojWIEQDjZJNyTBoBxP/NTwb0LT9iEEaw5prEUbJeIjixH8NS7OXXo9pGDQ9CxNFO8jHUKd+COKYmpPY0A1j9gcBSiV+cIBOGNPxo8QG10Qp2B9GY/9VLUVIMmYirWm4NlU7ohUYY//VXRNLQyuMU/8ZVG0LjWZ/GCUxdCzqVkwnMtkfBhP/KWgHkxjWbAuUpj2MGEYxVceiZimGGvaHIVprGp5N1YjYCw06aQ40PAtFTNuP6QcxZdukYhvE6XGR1tRdi6YdsB/Y7A+TGDY8G5OYbqjp+hGeZaQ5kPhhFMOagoFS7A1CAJqeRQlNK05sdczED6TjaOS/iqWIMNgfBKn/LBp2wF5g0xrZ4FoYCrpBTC/1X80xiLWRi2HDimnHJq1BgEqPcxW00xi6pkHNNUEn42GiY0aqYyGx1tRdm5oZ0QoNWn6aA66JQtEJQvpBnOiYZRCm4yEa5aGtaQfGOIYN18Imph2RyYHUf4PEf1XHpGIqAlQaw2T8eWZMN1A5HVM6ph3GDNIY1hxFqCf+S2II+wG5GFrEtEOd5IBlULMNUGocw7prUbE1gzR/RzlQ0ppWzCQPU9tbmRjWTPBJYjHKgbrlsx+mMTQMmq6JoZNYjHKgZqc6ls0BM6IbW+wPAwylkjxU0BrlgJn4AVIdi1Idsw38GPZGOeDaVM2I/dCgPY6hhYGmHUTjHKhaBrGCvTSGiY4FtCKH/cHHxNAx0UAr9V/VNWkYih6Jdo9iWDJj2oGa5KFrolL/DcKYcqoh0zkAewGTHPAsLKVp+5peEOHZSQw1kxyoOhbVcQwDFBP/FXVMF/Jwlo7V7Ij9T9SxpK9cDJ2YTmDSSmNY9yxsNJ1UQ2brWBILv6BjrhHRS2NoG6M5LKYbFHQsnQ8/LgdMYjrZHPgUOrYfazoFHeukMZypY14yjsY6Zhg0HHOGjplEsaLlh2P/NayYTmymc9FEx1rhJAdqronSitbH6FjDtakYIe3ILOgYdNIcKNkmtUIO1FyLmhXSDe1P1jE98d+N65iJ0jqvY7YiJK9jc45i19eZHLBZqrq3bc07i1hrdvsB+4MAyzCYL9lU3dtaMtxSbrelIfB/1Fp/TylVA15WSv2u1vqt23zem+LsXp/vbbbGn5erLksVh+9faY/bHj1cpzf0eW9nAICpFM8dm+ebH+2g0+/UXYtHD9f5zrnd8XEnF8ocb5Z46cIeAAp4ZmOOt6/sspt0hWcZfHl9jm+fnRx3uOby4KEqL6bHATyx1uBya8BmewiAZSie25jjG2d2xt9pejZPrNV5PmPDH7lrgRcv7NH1IwAMBc9uzPPC2W2C1PiybfLUkSbPZ2xYb3hsNEs5G750pMnFvR4XOz4Atql4bmOeb2ZsWKzYHKl7vHpp4r9HVmpc3O+z3Q/HNnyl4L+aY/LAco0Xzk/Od9d8meWKk/Pf00fnePniPn4UA+BaBk8daeb8t1J1WSjbvHm1M257bLXObtfn7H4aQ0Px3NE5vnlmYkPTszi5WOH0hf3xcfcsVFioWLyUtikS/53e3GYYJN8pWQZPH83HcL3hUbZN3t3qjttOrTW4sN/n8sh/xrT/5ko2jx+u891MDB84VCWOY97Z6o399+zGPN85u02UGl9xTL5UiOFGs8SxppeL4Y8fm+f5c7uEcXKgYxo8uzHHtzLH/dETC3z/SodL6VgDeHilRrvvc2Y/aTNTG76V8V/NtfjSkUYuB37ixAKnL+zTGoZj/z2zMcfLF3YYpsa7lsGzBf/90ZMLvH6pzdWuP257fLXO1Y7PxVYSw1EOZP3X8CxOrTX5zrlJ20+cWOSFC7vjHFDAc8fm+e7ZHcJMDjx9tMm3z06Oe/boHO9c67DTD8ZtXzrS5M0rLbpBMv5sQ/FsIYbzJZv7l6q5sfzgco2mDacvJnnh2vDU2jzfzviv6pg8sdbI5e/x+TJaa87s9sdtzxyd45XNXQZhYoNjGjyz0czF8FDF4fh8OWfDo4frWES8fCkZk2MdO7Od07En1hp859zkuLsXKqzUHE5n8vDHjs/z7TOT8edZBs8cnePbZ7fHx63WXO5byuvYHzq+wHfO7Y7z1zIUzxydm8qB43OlnC7ft1TBDyI+3EtiP8qBYgyLGrze8DhW0LEvrzd5/dIu/bH/FF9an+NbWR0rOzy4nI/hw8s1dnpDLrb9sQ1FHas6iZZmbbhrvsxyeVrH3r2yz06aF4+uVFHK4NVL2bnI4eHlGi9kbP8jdy3w/Nldhqn/TEPxlY15vnFm4veGZ3HPYmWsWSP/tQYBm6ntIx178cI2QZIWGR2b9LXe8CjZJj8o6Ni5/R5XO0leTHRsctxPnFjgva0u51O9hdk69tzGPM+f2SE1gYpj8shKLTf+js2VMFB8uNsbtz293uTVS/kc+PJ6PgeWKg4nCznwyEo+D03F1Fz+pSMNdvoB729PzndivsyJ+fLUXP7GpR3afnLkZC6fjKMvrzf5cKfHtYyOPbHaIIojXruczE9Vx+ShlRrfPZedyy0eW83n4U+cWOSF89M69trZHdqZHPjy0SbP/xA69tyx+VwO/PjxOT7Y7o/1FuCh5Rr7/SHnW5MceK4wD8zSsWNzZY42vLH/INGCb5/dGc9FrmnwzEZ+HjhUcXj0cH5d8IeOL/Dd87sM09jP0rEHlioMIs2HO5MY3rtYoTuMuNAejP33zMY8P9jaZjS8PSuZD7M58MzROd7b6rLVm8TwybUG1zoDzu1n12P5PHx0pcbuIODc3sR/9y1VmXcNTl9sjf2XrMd2cuuxZ9abLNU8Piuudob8xw+3M+sxix+/a4HaF6TAua2PpWmtL2mtv5f+vQ28DazdznPeLHv9gDcut3NtVzrDqe+9eaXNkWZl/DnSmve3ujywNGlrDUN6o1ki5f3tHn48+azTvp5aXxq3DcKYrZ5P2Z6E51J7OJ54R3z/cpu7FyfnC+NkwbNam1T4e4OAznBig2Mm1zgSQ4BYw9tX2zy62hi39YKI3X5AxoRkUlIqZ8Prl1vcv1wffw4izcX9AWv1iQ1b3YCC6bx5pc2hTKLGGn5wrcuJ+fK4re1HdPyI7Bk/3OlhWxOjNPDG5RarmfMNw5gr7SFu5nuXO0NUwfbvX26zMZ+JYaz5YKdHs2SP2/YGIYMgb/x7211ca5LgGnjzapsvr82P2/ppDBfKk77O7w+wzXzKvXG5zT1L1fHnINac3etx/6FJ224/oFsYR+9c60z5751rHe5emFxP14/Y6wekN+mApHCPMx6tuxZn9vrjyQTAj2I2WwM2mpP++2GcK2wA3rrS4WjWfzrxzXzZGbe1h8nOYpb2MBoXNpD47/uX29x3qDZuG4YxVztDHl2e+KHrx7nChvS4kwv5HPhot5cbf/uDZBdshMV0DmjgrStt7s3Y0AsitrsBy6VJrINY5xYEAK9dbnG4Xsp958J+n0OViR92+gF+xseQ5JzrTr7z1Nocb15pk/1Wx092EbOj5qOdHlUnP8G8frnF4cx48KMkBxre5HtXuz46bwJvXmnTLE9sj7Tmg+0uP7bRHLe1hiEdPz/+3tvuYqiJVcfnyry31R0XNpDo2LWuz3omFpvt4XgRDknRt9kajAsbSGJ4dq8/3qWAJAf8KG/8u9e6LGf8nuhYh7sz+dQLonQXYnLc+f0BuqAFr11qsVrP+k+z2RpQtifJs9Xzx4unEW9dbbM+N9GsWTrW8ZPxnknDRMfsaR17Yr05blusuLkbagBXOj69jB6t1lwutwc5nyY61mW9Mbme/UGy65bl3Wtd5sqT2Ix07N7FSQ6MdCw7js7vD3CKOnalzX1Lk+OCNIZ/9MTCuM2PdK6wgevr2KOrkzml60fsDyKMTMjO7PYpZ4UNeP1yuxDDRMdKmXngWtcnKubA1Q6WM/FDpOG9rS7PZGJRsq1cYQPwwU5vfDMGJjr2pfXJNSc5MKTiZGKtyRU2AG9cabFYmdhw71KVNy7lY783SHbgRzgW7Pb9mTr2lZMTG0Y6Nu9+vI69PkPHzu/3eezwJK5xrHKFDSQ5kF0LxRrevdbhf3Fycdw2S8fO7PZyWvfIcpUPd7q5uWgYxVxuD6Z0rJNZRFUdk6udYS43Rzr2kycmc3Kj5OQKG4B3t7o0M3N0sh5r8eThie2DMOZqx+dYZj6MYp0rbCCZy08uTrQnTOfyJzJjuWRbucIGEl+5zsSGkY49cnhyXC+I2C7E63bihxGvbe7n4tP2Q3YK13wn85m9c6OUOgY8DrxQaP9FpdRppdTpa9eufVbmXJcwjgkKixBgalEQxpqo0NgPIyqFqjaM9ZSTgzg/yfSDaOoEPT+iXFjAFCf37IJgfFwQUSmIflYsSpY5vrOVtyHGtfLHDaMIz8rbEBTOOQxjdH6dQNcP00epJhT9F2kwyB/YCyJKBdujWOcmtcSGot+nbR+E0dQEPCuGUOgriHJF0azjNNO+7wcRpjF9PQslJ9dW7GsYxaiCH7pBlBNzmL7mWCe+Kdrg2UU/xJQKvsna7llGMv4KdP2I+YztxbEHyQRSvJ5+kDz2UDzfaMo0mR5D1zuuG0QcymzFzzouiDW6EMOuH08t/rM5V/Gs3GLw42zoBxGHMovzcIY2+GGMYxZi6EdU3evnISQxzMbVMWbHYhjqXEEP0+No1rjt+hHVohYUDgxjTVjQo14Q4doFHYti8j3lfVp2zKkbOaO+DhUep8iOpYprzTxuVixm5WFc1OAgwpsa7xrTyPc1S8eK/pvl0+LcEGkoCuAsHfPDGLPgwFk6Vux75njL+H2uZE/d+BjZUIz9LP9xA/nbDyKaBT2a0rFwWsd6QZR7jGVW/l5XxwoxDOIYs1CQ3kgODGbEtejTKNZEM+bkbAxn2Q6z54GCmcmcnMmnWTENoryWOqZBP5yOay7nLAt/1lweRkSFWAyCiIXqZE6eZcPwOjqWvVnlx7NjOBWLMJ66EepH0zqWvZ6qa+UK96wNlcK8lo1H1bFm6mYviLDNid+L42zE9DiKiWesCw5VJ36YmZdRPNVX14/GjwACU2tGSFKwuCYczJzLp6/xdhFpZsZi1rx5p/KZFDdKqSrwW8Bf0Vq3sv+mtf41rfUprfWppaWl2R18hlQdi+VKfkFqKFAFTy2UHXQhzkcbJd7JPPYEyZZ69mtl26RSEO6jzTK7vXw1v1x12crc3bEMlTwzn2Gl6tIq3BVfb5Q4uzvpS0FukbU/zIvViI1miQ93urm2+ZJD25/075gqJ9IARxoevWHehrVGife2J34wFBTqDOZLNi0/f9xGs8SZnX6urWQbuTttnmVQsvOdHWuWuNzO+2+x4tLJ2GWqKa1lqeJMieKRRinnd0XyqF2WimNSLsRwo1Hi/G7ef8sVlx9sT9osQ00txA/XXPYH+bsh640Sr23u5Wwoxr7uWlOLiY1miTO7+TtT82WH/dzOnZFb9Gz3A9bq01vda3WPNzKPw9RcE6tQvM2X7KlJ/2izxLVufoen4dmMohrBzG3to80S5wq2H655/O4Hky39Wvr+SZblikO3MP6ONj3O7E3GkSqcc38QMlfKF98AG3PT/lusOrxxZRLDkl0syRNfXe3kY3ik4XGuYENx3DY9i5I96e3D7Q4bcyWKND0rd1fStYypyXWjWeZyYWftcM3jUmvSZiimFq4LZWeq7WijxJuXczJNzbXIZsroef8RZ3Z7bDSnbV+uuryceZSsqGMX9/q5XdcRa3WP7d7kTqVKjy3aVCwQkhzoFr5n5hahjmlMLZaONEtcLuzQr9Rc9gcTGwzFVMEwV7KnFqEbcyU+KtwhbpRssptfs3TsaLPEdneiY6aCxcJcZCpFLVO4v3O1w2pt2u9HGyU+2s2Pv1k6VlwwzdKQQxWXs5m7zfYMHVutuewNpnPgW2eujD9XHWvKhkTH8mw0S7y/nY9h1TFzhaVrGlMLxY250lQOHKq6uZ1jQ03n4XzJxjOLsSjz1pXJuPVsI7eLB0k/xfFwdK7ElXZ+DluuerkdZ882pnWs6uTmyIv7fY428nFVkLtpszcIaV5nLvcLcV2sOry3PbFrpo41pnVsve7x4vmJBldtE7tgfNOzp8bR0WaJ83v5GDbcaR2rZnz65tUOR5vTc9HhmpeLq6nyen65M2S5Nq0hRxsl3szEUM3Qv7JtTi3YN5olhoW1yaGqy4sXJn2VZsRwperSD6bXY69cnDwKahpq6qZr3bWm1hNHmyU+KKzHFmfE+nbhWQYnFspT7bPmzTuV217cKKVsksLmN7TW//J2n+9m8WyTR1YbHGl46cvpFj92bJ6FkkXTszFUIuSPrdbpBCGeZWAbivuXqixVHRarLqahqDrJ8/pl22Sx4mCoZDH95aNN+n5IxTExDcWJ+TLH5kq0g2TS8CyDJ9Ya1ByT1ZqLoaBZsnl2Yw4Dnb5kn0wcD67UiElEwjENHlqusVCyWa27ySToWjx9dI6SUiyUE9uXqw6V9J2Usp0sWO9eqLDW8Ki5FpahKNsmp440qNgmK9XEhvmSzTMb84RRRM21MFWSgPcuVccva7qWwSMrdZquxUrVw1RJ4j67Mc9CyWGulNhwuOby+GqDpYpDKfXffUsVlmsuyzUHy1BUHJMvrzeZK9kcSv23UHZ4+ugcQZC8wGcqxfG5Msfny6zVPWwz8d/jq/XUD0kMm57Fc8fmWSjbNFP/rdU9HlmpE8Y6iaGpeOBQlUNVh/VGCVONYjjHXNlmsZzYcKji8KX1Jt00hpahOLlQ5uhcCctKhL9kGTy51qDmmhxOYzhXsnluY56FikM99d96w+OBQzVircYxfHi5xlzJZqlaGov4MxtzOEoxn/pvpepy6kiTQRSNY3jPYoXVusdSxR3H8KkjTSqWwXJ15L9kHIVBnMZQsV73WCo7PLRcG8fw0cNpDDM5YKB59ugczdIkBx5freNHepwD9y1VWa64if8yMazaiqU0hosVh5KleHq9mcTQUNw1V+b4XIlmyRnnwOOrdWq2MckBz8aMY57bmM/lwMOH60R6lAOKB5drLJQcDtfc8ULw6aNzeIZiIY3hcsWhbCi+lMmBkwsV1uoei2Vn7L8n1xpUbSOXA56heHZjbhzDo02P+5aqHK65if9Mg4dXasx5yfib5MAcJUONc2Cl6vLEWpPtXkjJNrAMhetYrNc9Ti5UkhywzdRGg+VMDjxzdI6Fsk3NsdIcKHFivsxqw8NJc+Cxw3UansVqJobPbczjpL4c69jhGle7/jgH7l+qslix8WxromPrTTxLTevYMBrnwHLV5VDF5b6lyjgHnlhN/He4oGPoiY6tNTwars2jh2s5HVuqOKw3vLGOPbORXPP8WMdcnjrSwExjZRmKexYqrNXdXA6cWmuwULLzOnZ0jiiK8zq2WGG15mV0LNHStUIMDcjp2BOrDUyl8jpWcVmuuTkd8ww11rHFmTpW4sR8iWHEWMd2+gGPrtRYy+jYsxtzVAw91rGVukfVSeKd1bHFsj3OgayOLWR07MvrTRbLTl7HmiUWK0keluzZOvZsGousjt1/qIrWFHTMouxMdCwKI549Ol/QsUby4wJZHau56Y/qJDH80pEm856d07FnNuaYL9ljHTvWLHFyPsnhiY6lMczkwLMb89hKTenYtV6Q07FDFZuyY491bOhHfHm9mdOxp9fn8IfhlI6FscrpWN0xcnO5k75TkdOxlTrXusFYx2qezcmFCsfmSjkdc8y8jlVm6Nh63eNS2/9YHSvN0LF7F6d1rOnZzJcnORDFMc9szBV0LMnDkY7du1ThcNXBj9WUjh0q6JifyYG5ks1CyeaB5drH6tizG/N4ps7omEfdMXl8NZ8DSxUb0zDGOmaq5F2Z7Fz+9NEmi2V7nAMn5stsNEtc7YfX1bG5kj1+r3IUw/WGx0PLNXpBnNOx+bLNXMUd54Clkvedsjp2Kn2fq6hjdcfO6VjV+kz2IgBQSnFiocK9i9Wxjn3l2HzuaY47HaVnbJPdss6Tlxz+CbCjtf4rn/T9U6dO6dOnT982ez4NQRjTDSIcU40fD9vvJ79m4ZkG5fTOwW7fBw1zaVUdBAHtIMZQimY6ENqDgCDW2AbUPCfTV0zVUjiOw3A4pBspFHr8HHQn/WU0UykaacW8N/CJ4+QRlmr6qMBuz0fDeEdmGAR0ghgTNb6zMwii9BElAze9W7LXC4gp2BCS2J4e1/F9/BAsUyW/2Abs93xCNGXboGTbYxtg4odBENILYgwDml7eD55ljH262xuiUVRMjeu6+L5PJ9QoZYzvErT6PqFOir9a+rjbXt8n0pqSbVBObdjp+SgFc6nfe8OQQcF/oxi6pjF+hHC3n7yLMPJfLwjoB8lxxRhaCupp224/QH9CDNvDkCAajYd8DMu2gWdPYpj1Xz8I6AUxFopG2tYaBoSRxrGg6jhpDH1iralY5PxnYIyfJe4MfPw4uWs0elxwr+cTFWK40/NRGRs6gwF+pHLjYb83JNIaRymq6TXudodoyNjQpRMkk2Zj5IfugACwgVoluTu31x0SAzUnwrbL475AMZfese71hgy0xkTRSJ9Jb/V8Qh3jGlApJX3tpLtF8+l3ev0e/djEBJpp235vQKTBMRTVkjsZfxqqdjEHoDnKw76PH8dYhqJeGvU1JNJQMmJKpdLEdsU49v1+n35s5PzQ6g8JY42tFLXr+s+nE+hkLI+O6w2SHFBQK0/8FwElI6JcKs/0Q7c/YBiDpQzqoxh2h0RoXBSVysgGH9DMpZ+DoEfbNzEy/mv3BgQ6H8OJ/0IcpzL2n4JxX53eEF/rJA/T6xmNW8fUVL1RXwO0VmPb+/0+vdjAVJpmes2t3pBQ61wM93pD4huNoVLUy5PxEGpFORPDne4QpTRz6flm5UByvhvLgVwMuwNCbiyGWf91+0OGcT4HxjE0FJXUDzeSA6MYWgrq5WIM8/7L2tDuDQm0zuXAyO9lU+N5k77Qk+NGMbSUpjGKYZoDjmFQLTm5voo6lujRKIZD/Fin+ZT6rzcgmhFD0MynY7Q7GDCMVBr7fA7kY+ij0VMxzOXAx+jYKAdG4+GW6FivR1+bmGia6flurY5N58CdrGMzcyCnY8lxc5kcGMSzdcwC6j+EjiVacPt1bOS/bAw/a2KtGQQRhqGmHhW9U1BKvay1PjXVfpuLm68A3wTegPHTWX9Da/3vZn3/TipuBEEQBEEQBEG4M7lecXNbf9NNa/0tmHq0UxAEQRAEQRAE4Zbz2T3EJwiCIAiCIAiCcBuR4kYQBEEQBEEQhAOBFDeCIAiCIAiCIBwIpLgRBEEQBEEQBOFAIMWNIAiCIAiCIAgHAiluBEEQBEEQBEE4EEhxIwiCIAiCIAjCgUCKG0EQBEEQBEEQDgRS3AiCIAiCIAiCcCCQ4kYQBEEQBEEQhAOBFDeCIAiCIAiCIBwIpLgRBEEQBEEQBOFAIMWNIAiCIAiCIAgHAiluBEEQBEEQBEE4EEhxIwiCIAiCIAjCgUCKG0EQBEEQBEEQDgRS3AiCIAiCIAiCcCCQ4kYQBEEQBEEQhAOBFDeCIAiCIAiCIBwIpLgRBEEQBEEQBOFAIMWNIAiCIAiCIAgHAiluBEEQBEEQBEE4EEhxIwiCIAiCIAjCgUCKG0EQBEEQBEEQDgRS3AiCIAiCIAiCcCCQ4kYQBEEQBEEQhAOBFDeCIAiCIAiCIBwIpLgRBEEQBEEQBOFAIMWNIAiCIAiCIAgHAiluBEEQBEEQBEE4EEhxIwiCIAiCIAjCgUCKG0EQBEEQBEEQDgRS3AiCIAiCIAiCcCCQ4kYQBEEQBEEQhAOBFDeCIAiCIAiCIBwIpLgRBEEQBEEQBOFAIMWNIAiCIAiCIAgHAiluBEEQBEEQBEE4EEhxIwiCIAiCIAjCgUCKG0EQBEEQBEEQDgTW7excKfUPgZ8GrmqtH7qd57qV9IOA9jAGoOYalGyb/X7AIIwwDcVixQVgu+cTRDGeZdAsOfi+z76v0WjKtkXVtWgNfAZBjGEoaha4rstuL2AYRbimYq6c9LXVHRLFmrJtUvNsuoOQbhihFFQcg7Jts5f2ZRuKhaINtkHTc+gFAV0/RmtNxbaouBbtQUAvyNu+2xsyjDSeadAsOwyHQ9ohxLGmZBvUPIfOMKQXhCgUDUfhOA57PZ9BFGObBgtlJ2e7Z5k0Sjb9IKAzjNFA2TKpehatYUDfj7BMxUJ6zTtdHz+e+C8IAvaGMRpN1TEoOw4d36fnxygUdTv1X99nGMY4psF8wYaSY1J3bXqDkE4YodIYep8Qw5Jp0Cg7+GHI/iBCo6k7Fp5j0R749IMYZSjqaQx3ej5+FH98DIch3SBEKUXTMbBtm9bApxfkbd/uDgliTdk2qI9imPqvYplUPIv9QcCgEMOd3hA/0rimyVzZzsXQswzqJYf2MKRfjGHfZxDmY7jdHRIWYljMgb10zFgKFqpeMo66A4YxeIaiWXEnOaA1ZcugWnLo9If0Qo2hFLVRDNO+HEMxXxn5b0AUQ8lU1MsuncGAXghKQ8WKKZfKtHo+vSifAzvdIX6sKZnQKHv4fpe9oQlA1VSUyy7t3oBeBKaCxdT20XEjGwaDQeI/DWUDahWPXm9IJ9IooOFGOE6F/d6AfkTO9lEMS4aiUXHp9/t0IpXmAFQ9j1ZvSD/SmAYsVkY2DPBjxuNoOBzSCkj9p6iWXDp9n14Yo1Qmht0hg1jjGDCf9rXdGRBqKFmKeimxoR0pFFA1NaVSif30OFMpFqup7Z0hgdZ4BjQrXj6GpqJadmn1BgwiZsbQNRRzhRiWTaiVPbr9Ad0QFJMYjjUkq2Op/0Z61Ov36IZGmgOKSikTw4z/drtDhrHO+a8dQKw1ngn1skenN6QX6YL/BgxisJViIfXDVmdIpDXejBjWLfA8j1Z/SD/M58AohqMcyMcwnwNKZXRsnAOTGF43Bwox7Mc67780htkc2B+a6GwOdAf0Y1AKaun1jHIgF8POgEhnYtgd0o2LOZCM5Vk5UDYN6tkYKqhYULluDqQ2zIjhJPbJcbNywM7EYpQDnqlolCc5AFAb+a83ZPApdKxkKmpl94fWse4gzYEb1rHE9qyOVQxFpfLpdExrKN1OHcvZcNB1bEg31J+rjgmfjtta3AD/GPgV4J/e5vPcMra6Qz7Y7nFmtwfAXfNljs2VeWVzn51+gGMaPLJSY6Fs8M2P9hmEMXXX4om1BnvtIW9sdYg0HGl43LdY5ftX2lzuDLEMxf1LVZarmu+e36PjR5RtkyfWGjhmxDc/ahHEmqWKwyMrdd7f7nJur49ScHK+wtGmx+mL++wNQlzL4LHDdQwF39tsMQxjmp7F42sNLu0P+MF2F61hvelx90KV1y+3uNb1sQzFQ8s1DlUcvn12l24QUXUSGzrDgNcvdwhjzUrV5cHlGu9udbiwP8BUcPdihbV6zEsX9mkNQzzL4PHVBq7SPH+hhR/FzJVsHl9tcHavx4fbif+OzZW5a77Mq5dabPd8bFPxyEqdmmPywoU9+kFMLfXfTs/nrSsdIq1Zrbncf6jGW1fbXGoPMQ3Ffan/Xjq/T9sPKdkGT641GQQRr11K/LdQdnj0cJ2PdpIYKpXGsFnm5c19dtMYPna4jmMqTl/Mx/Bae8DbW11iDesNj3vSGF5JY/jAoSqL5ZgXLuzT9SMqtsnjaw3CKOT0xTZhrDlUcXh4pc572x3O7w2SGC5UWK97nN7cZz+N4eOH61gGvHShxTCKaXo2j6/VubA34IOdJIZHmyVOLlR47XKLra6PbSgeWqmxULJ5/twevXEMmwwCn5c3O0SjGK7UeOdah4tpDO9ZrHK4FnP6Yj6GBjEvXWzhR5r5NIZndnt8uJPE8Ph8meNzZV65tM9OL8AxFQ+v1Jl3DL51fp9+mMTwybUGW50hb19LcmC15nH/oQpvXe2MY3j/UpVD1ZgXz+/ncmAYRLyaxnCx4vDoSo0PtnucTXPgrvkKR5sG39tssdcPcE2Dx1YT/52+mORAw7N4YhUutwPe3dpDp3l4zyK8cbnN1TQHnlyr4ZgW37u4TzeIqDgmT6426PiTHFiuODy8onh3q8P5/QGGgnsWKxxpDHjpQhJDzzJ45midrg+vXsrmQJ1ze0M+TGO4MVfixDy8eqmd5ICR+K/mmrx0YZ9eEFFzLJ5Yq7PbD3jzahLDwzWXBw7B21fbbLaHmEpx71KF1WrMCxf3aQ9DSpbB42sN7Djm+c0WQaRZKNs8drjBhzt9zuz2Mzpm8L1MDpxaq6ExeGUzmwNM6di9i5o3r3RyOnaoGvNCIYboiO+ebxGOdQze2+5xPqdjRk7HvrRWx48T/411bLXBxZbP+zkdg9cvtyc6tlLjUNnmW2cnOfDseoNL3YC3r2Z1DN7d6mZ0rMp6XfNCRseeXGsQxjGvbLYLOjbI6FiJu+YVr17aZ7sXjHWs6pi8eH5vnAM3omP3L1U5XNN891yiY2Xb5Jn1BruDiDcuT3TsscM1PtjpcXa3P9axjabie5utnI41PcU3zyYxbHgWTx2BC/sBP9jaG+vYvYvwxpU2VzqJ/549WgVf8/LFvI7pOOSFC1kdUzkdu3uhwtHGgBcv5nVMKfjexVTHSjZPrNY5v+ePdWyjWeLEArx2uZ3Tsbpr89KFrI416PoBr17K6Niy5p1rXS62khjeu1RlpTrRsVKqY6GOeXVzomOPrTY4szPgo3QuPz5X5q75JAeSuTyJ4Zxt8M0L+Xmg1RnyWqpja3WP+5YmOWAaigeWqixWkvlwlAOPrzWwiHn+3P51dezEfIWNpsHpjI49ulqn4cA3zk507Km1Buf3A97bzuiYzuvYQ8s1Gp7N6Qt7Ex1baxDFAS+cT3Ws6vDw8ifr2FNHGgxDPUPHBny40xvr2Ml5eKWgY0ueybfO53WsPwx4+fLH6NihKocrMS+OdMw2eGa9yf4w4vXLH6NjC2WON43cXP7o4RqeZfBSJoZPrsHl9pAffIyOPXCoynw55vSFvI65ZsR//OjjdWy9kdgw0rFn1+v0woKOrTW4uJ/VsRJ3L+ixjtmG4sGVGotlm+fP5nOgHwS8spnXsaWqFDifhtv6WJrW+hvAzu08x63mWtfno90eGtDABzs9tns+HT8CwI8SUe2HikGY3NluDUNOX9jjUNMj0kk/F/YHnG/1MZObRoSx5o0rbXpBPO6rF0S8cG4XhU0Q6/H537nWYbXuoknuIv9gu8veINlFARiGMS+mBdIwtWFvEPK9i/t4tkmsE9vP7Q243BniWWpsw6uXWnSDiG6Q2NDxI144t4dtmoSpDZc7Qz7Y6bFSsQGINLxzrUvHj+gOExsGYcwL53dRpokfJTbs9gNeu9TieLM09t9Huz22ej5xnHwniJIJ1Y80/SBpaw9DXjq/h2eZRDqxYbM95Oxen3Z6vijWvHmlzXYvoO0nbf0g5jvndukF8dh/2z2ft660Wa7aY/+9v91ju+/TGQbjGL54YY/9YZiL4csX92mWXdKuOL8/YLPVxw+jsf9ev9ymF2q6aQy7QcQL53cpOfbYf/vDkM3WgHN7g0kMt7ps9QJag0kMXzi/R4xiGI1iGPDqZouFsj2O4dm9Ple6Q5J7PxDEmlc2WwxCTS8TwxfP71L3XKJMDD/c6dFwzHEM377WYbsf0CrE0DJN/HTgdoOI7Z7PBzuTHPhwp8eVznBsu5/GcKgV/bAQQ9sc50DDNfhwt8+l9nAcw+9fadP1dS4HvnsuKbRHMdzq+rx9tcOxudLYfyXb4JV0QQAwjJIcaA0nObA/SGLoWpMcOL8/4FJ7wFrdGcew4ti8cH53nANdP+K75/dwLGscwytdnx9sd7l/qQypDe9c6ybnG0z8F2mDFy/s5XLg1c0WnmWMbTiz2+dyx6eVjr8g1nwvnRhHMWz7YbJIDuJxDC+1h5zZ69FOfRVpzVtXO3SCaJwX/TDmhXN7mLZFMIqhH7HV9flot5/TsZ2+j5Xmlx/FoAxeOL/7sTrWdE0+2OlzuTMc+++NGTF84dwujjXJgUEQc6Xjc26vP6Vjw2iSAxGKF8/v5XTslc19js+Vx/5bKju8u9XhWtcf2/DqZotuEOdyoBNo3rjcLuhYn1Kqf4mOdWj5YU7HvnNul64fT+nY4Zqb0bE+W12fXnrNIx0LIj2VA3OendOxc3t9UhPGOdDx47GO9YKIYQzf29zP6dibVzo4hsrp2NWuT2uQ17FhNJmL+oOQ1jDinWvdnI5dbA14cKk69p9jOXz33N6Ujnn2JIZXuz7vbXXpDKOxDe9uddkbRnQKOtYeRhMd6we8stmiZGdyYK/P1a7PII3XSMf20qcKRjF88fweFcfO6dhHu5l5QMNbV/M61g9jvnt+FMPkuJ1+wPcvt+iH0UTHdntc7g7Hx/mR5vTFfYYqP5e/dGGPhfokB+I45qPdSQ5EaQ7s9MOpHLAMc0rH1hre2H/vbXfZHYT44UTHXjq/hx+b4xxoD0L2BiHvpjfZRjq22Rqwn9o+msv3BkFex87tUbKdiY51fN7b7nJyoZRcy0jHBhGDnI4xpWOvXWrRD+Kcjl3tBgThJIbf29ynF5PXsQt7NEqTuSiMYs7t9dkczQNa89aVNt2sjgUxQcw4p5IcCPj+lTa2aUx0LJ3Lu5n1WFKkRVMxHERxbj12sTUYX99oLt+dEUOY5MC1rs+7W11OZuaiH2x3afkRg4yOxZjTOnZxn3JuPdbnSsen6Zpj/726mfg4mwMvnN+j5jpT67FePynShRtD3rkpcKk1mGq73B6yVndzbZ1hlP/sR+PF+ojN1pD1ZjnXtj8MqdqTDbMg1nTTomVsQ3tAxclvql3pDDnamPSlgSh/uuQujG0WbBhw90I11zYShhHDKCadi3PHNUtOru1a12djvjT+HGvGwjBiu+eTb0n6um+pkmsbJXP2c3EwbrYGLFbyNnT9CMecfHMkoFkud4ZUHDvXdqU9ZLVeyrUV/dcehiiVb7vYGnKkkT+uMwyxMsYGkWaQif1CyRkv6LPs9AOq7iSuGnLHQTKpOFbeE5utAXcv5v3X8fNjZhDG9As+3WwNWK7l7/aM7nSOiDX0Mjas1d2Ztl/r+jS8vE+Lse+mj82NOFwvzcyn1iDI2ZCIeN7xl9pDbGPynapjsZsWNiNm5UBrODsHVjJ3vfrBZBE0wo/iqbF0qTVAF0bl1c6Qx9cb48/FXIIkzjW3kL/tIXOlvP+Cgg399FHBnO37AxbL+RzY6QU8dGgyHiKtc3asN0pstqf9fqk95LH15vjzMIwppk9Rx5aqHpszYtj2w1weBrEe33wBONJwuTjjuCudIU+tzo0/D4KYYgbvDUIG4eR6GiVnpg3Za246xnjRmmWzNeBwLZ+/W12fjWZex4p+SO5MF2LRHkxpwSwdiwpiutkacHQuPw/s9n1Ozk/GZNeftv1yZzh+BDVre72Qh+3MXHT/4RrXOv5UX5vtAY49uZ5eppgbEUQ6pwWj44oafLUz5OjcxA+jRV/++oKpOWyzNWCtntejYg4MwpgwmvZf0YZ2uus2ItZMzWFXuz5zxTmsM0PHCnN5158slAFWG6WZ468fRFgZvQtjPS40RlxqDykV9Ohye8hDyxMN0eT1/FDV5Wp3OoaX2sPxY8QjgijOKacfxfT84jpkgGXkbbjW9XlkrZ65loKQkhQXRV9ttgecWMiP5eJc1A9iepn8PdIszdSC3X7APQuTcVScTyDRi2LsL7WHrNbyeREWBmDHjyhZ+WtO5vL8+BuEMWZm0p+5HmsNMMz8/HSlM+CxlWbmfOFMHSvG/mJrwIlPWo+FcW78JTYMGcSyXP80fO7eUkr9olLqtFLq9LVr1z5vc6aSGaBRml5YuYUFqGWo3GQPUPcs2sO8SJVtk34meRTgmvkEqLnW1GTR8Gy2evlFZ+F0uKaBLih8w7PYKRxXtNNQ5ER6ZENY6KvmWlxt5/3gFfxQts2cWAA0PZur3fxxRRtMpVCF66m71lTiu5ZBUJiUi35I/Je3ve7ZUzEsHmcbCqNgeyN93yWLZxlktUeRHw/dIKTuTT/xWXHM8Z3LEU5BNF3LoKiSDddmq7BgKfrdUEn8s9Rdi2HhfCXLmFrUZG3f7Qc0Zthec8yp4mlWDmSvph9EU4t8gLIzuUuZtT93PtdKHlJPCdP3iIoUY+jMyIG6Z41330Z2F06HYkYOeBaF8FB3bc7tTvKp6HMYjY/p3OkVxnLx0ORc0+O2ONlWXIsLrW6uLRuLnb5Pc4aONT2LS/v98ediDkKSA9l2P0oe8yjiFcZRUcf2+gHNGeOo4dmc3ZvcgXSsYiSSa8kWeeF1bMjauefHUwsJSHKgWIBUXWtKj4quKNtmsd6mMUNDpnTMULkCH5Lx1ykUXhXH4sLOZME3KxY116IfRlNtxevJ5sXm/nCmr+quhckkXo6pZuaAa07PA0UNrnsWW4XFd9F8zzKmbhY0XJv9Qd4PxeMMBVbBhlnzgHcD80DFMXNFcnI9Zq4Ih+kctgyVG3+dYThTxxxz+hrdwoK67llTRVfDs7iYycOiDfuD4LoxLBbBZrqzN0LB1M2xmmfN1NfzexMdK85DMHuuaHgWW72PXwuZSuXa2oNw5vVUHIvLnYkfimMPoOqYUzcAm57F7uCT5/LpNcD0XG4bKnczQgHe1HrMpjhj1F2b8xkdmzU3uZYxdaOj4Vns9fOFXnH8GWpaD2qehT3tHuFj+NyLG631r2mtT2mtTy0tLX3e5rDeKFHK3OEq2yarNS8nymt1j6qTH2mPHq7T8yeJ45iKuxcqvLs1SYD5sk3NNXM7G/cfqmJnFnGmgkdW6ryyOXmar+qYHKo67A8mRx6bK+XSTQGPrtY5uzs5n2sZHJ8r88aVzrjtUMWh7uaT96HlGtc6E6EbPc/7/Nm9cVvdtVgoO3QyE8OJ+XJu8adSP7x/bbLwKlkGR5re+LlngNWai10QskcO17jcmgidbSjuXaqOH0MCmCvZzJWsnJg/cKiaKxgMldjw2ubuuK1im6zWvfEWOCTPgBe19NHVek6wHNPgxEKFi5mdjMWyQ9nJ+++B5RrdTBHbGUbcNV/OCXzNtThUcXKL3uNz5Slhfexwnfe3J/HyLINjcyXe25nYtVx1crt/AA+v1Gn18zF84FCN05v747aml8Qwe2P07oUKYabQ2B+ErNW9ZHGXUrZN1hql3EJhre5SsfPy8cjhOhf3J3ae3tzngeVarmiYL9nUHIvsdPXAoWqub0Mlfb2SieGZnS6PrdZzY36jWUJlitGR/87tZSdMg7vmK3z9zN64rT3weXC5lrP9oeUaO92J/8w0B7774SQP667FYsVhs5NdlCqOZu4GKuCx1Tof7UxywLMMNuZKuUXp4Zo7dWfx0cON3Hi3DMX9h6rsZhYTTc9mvmSxl5kf712s5Hy82w840vSmdOxwzePNqxO7/DDiZOEu7CMFHXvpwh4PFmNYtqkWNOT+Q1WCaJJfV7s+x+byOTDSsXP7Ez/HseZYZhdgFMNLrck4evniHg+v1HP5OkvH6q7JYnlS1FmG4sHlGq9fbmW+Y7FQtnM6ds9iJZeXIx175+okD0uWwXrTY6c/yfOZOrZS41ImB0Y69lamr7mSTdOzyC5xKo7JSnVyN3qkY+9tdXLfOVxz8TP5ut7wqGRy9VrPZ7Hi5BaTjmlwcqHC77w/ySdDxTxUyIEHlmsMMn4xleLhlRrbmUKm5loslZ3cXfa75su5heQohmd2p3PgaibHVqrOVA48vFLnWmbX0TIU9y/Xcn5vzNCxexYruRsYhoLHDjfGjzJCkgNH6qXcjZW1ukvZLs5FdVrdiYZ8uNub0rGFkp0ULpnj7l+qouNJ38Z15vKVmstme2LX0aaX09JBGLNUcXIFlWsa3LVQzu0yHao4udhDomNxJg8THavznRk6djkTC4VmvaBjj6812Mp8x7MMjjbyuzArVZdqYT58+HCNwJ9c39m9PvcuVbEz/mt6yVzeytx3LdlmbkcmyYEGH2xNxlHZNjlc98aPSEPyPo1VuCn52GojN2ZG67GLrexcnqzHsjwwYz328EqN756dXo9lY2gZKrcbPM6BzDzgWgbH5sq8dLE9bjtUcXJPcwA8tFxnv5fPgQcOVanJjwp8KlTxLuctP4FSx4D/7438WtqpU6f06dOnb6s9N8JWN3m/QClF3TOpGJq9INl6dE2DimsCit4wYhBGVByLkmkQkTyuEceammexVHG52hnQHiaP69RcE0MZ9P3kWfuSbVKxDLRStIchQayTRXDVzdvgmpRtxd4wpjsMcS2TqmOhdbINPgwjqo5F3TPoBZrOMCLWmrpnsVhxudIe0PEjbENRcS0sI6Yz1PSD5CW6kmOhY03bDwljTc01OVT1uNYZ0h6GyS+9ORYm0I9iun6IZ5lUXJNYa3p+8rx11bGYcxTtMHlUQqc2VIyYVmjQ8UNsQ1F1TAwFnSBmECT+q9omgY5pDSPiWFNN/XC1M6ST2lB3TTzTYG8Y0fOTx4/qTrKL0vGTdzaqjkXdiunGxth/NdekZsGur8cxrDomKEU3E8O6ZzAMoDWKoWuxVJ3E0Er9YJjQG0bjGFZdRRgbdNMYVh2T5VrGf0pR8yyqjsFuL0xssEzqrkmsFR0/TGLoWtQcxSCEVsZ/ZRXRjoxxDKuuhaE13fRRtLJjUrOtsf+ibAy7Q9qD1H+Oha0UnTBKYmibSaGmk/cn/DSGTRu6kcrZUDU1+0H6OJJhUHUMTK1phyT+s03KtibUBu1hTKzj1H8e19oDWn6IaRjUbRNbx7TT57RLlknZAo2iE8QEcUzVNqlZmm5s0B4mvxhYdy1sY0gvcFL/GVRNA2Wk4yhMbK8aIUPsJA81kxi2B7T9ECu13dLQiSY5UDYVsVK0/Ygwjqk5FofGMQySGDomnopoRQZdP8KzDCq2Am3QCZN3f6qOxZwb0g4SG7SGhmtSTv3XDSJsIznOiDW9WNEPExuqCkLDoBVExHGc5oDHtc4gHUcGNdfAUjG9QNENIjzbpGpotGHQ9mP81PaGDZ0IWoPUf45JxRqyF7iJ/wwjXRjF9ELNIIypOCYlMybSJm0/iWE19UPOf7aJoWP6oxjaJhVLoTW00xiO/LfVSd5xMFQSCyf26WibbhrDSlr8dMN47L+qETJQNp1hEsO6a7FYHelYiG0Y1GwDpaAbZnTMIPVDIYap7aMYmiqin42hpdAYiZbGIx3z6QQOLT9Ca8bzQCtU4xyoOQYqjulE6hNz4GpnkOiYMqg7JlYc09GTHKiYmthQdHyd5IBjUbf0OA+VgppjUbMDdofWRMdsE1RMN5jEsO5qBkHih1hraq49lQM1x8TQml6kJzpmKUKg48czciCNoWPhEtCJrXEe1mwDHUMnmsSwYgf4sUNrmORA3bUoGxGdyKCdxrBqGyg0vYhxDGsGBCrJgSiOqTsWS7kYZnIgVEkMbZOyCShFJ82BkY51QsbvrNUck6rFlI6hExsG6Uv5ZevW6lgvNmmljzzXXQvH8OkG9pSOtYN8DszSsVEOjHUM6GRyoGwpYm5Cx4LMXO76tAN3rGN1NxmnrVCN87BiK0ydjNPboWN1S9ONVU7HqrbPru/kdEwR0/0YHaul46iYAyqerWOtIMmBqmOxXNCxqmvh6YB2bH2sjlVUgG8kv1j6aXUsVkkssjEUZqOUellrfWqq/XYWN0qpfw78YWARuAL8n7XWv369798pxY0gCIIgCIIgCHcu1ytubutPQWutv3Y7+xcEQRAEQRAEQRjxub9zIwiCIAiCIAiCcCuQ4kYQBEEQBEEQhAOBFDeCIAiCIAiCIBwIpLgRBEEQBEEQBOFAIMWNIAiCIAiCIAgHAiluBEEQBEEQBEE4ENzWn4IWBEEQBEEQBOHOIwgCLly4wGAw+LxN+Vg8z+PIkSPYtn1D35fiRhAEQRAEQRB+xLhw4QK1Wo1jx46hlPq8zZmJ1prt7W0uXLjA8ePHb+gYeSxNEARBEARBEH7EGAwGLCws3LGFDYBSioWFhU+1uyTFjSAIgiAIgiD8CHInFzYjPq2NUtwIgiAIgiAIgjBmb2+PX/3VX73t5/lX/+pf8dZbb93SPqW4EQRBEARBEARhzKctbrTWxHH8qc8jxY0gCIIgCIIgCLeVv/7X/zoffPABjz32GH/1r/5VfvInf5InnniChx9+mN/+7d8G4MyZM9x///380i/9Ek888QTnz5/nb//tv819993HH/tjf4yvfe1r/N2/+3cB+OCDD/gTf+JP8OSTT/JjP/ZjvPPOOzz//PP863/9r/lrf+2v8dhjj/HBBx/cEtvl19IEQRAEQRAEQRjzy7/8y3z/+9/n1VdfJQxDer0e9Xqdra0tnn76ab761a8C8O677/KP/tE/4ld/9Vc5ffo0v/Vbv8Urr7xCGIY88cQTPPnkkwD84i/+In//7/997r77bl544QV+6Zd+id///d/nq1/9Kj/90z/Nz/7sz94y26W4EQRBEARBEARhJlpr/sbf+Bt84xvfwDAMLl68yJUrVwDY2Njg6aefBuBb3/oWP/MzP0OpVALgT/7JPwlAp9Ph+eef58/8mT8z7nM4HN42e6W4EQRBEARBEARhJr/xG7/BtWvXePnll7Ftm2PHjo1/mrlSqYy/p7WeeXwcxzSbTV599dXPwlx550YQBEEQBEEQhAm1Wo12uw3A/v4+hw4dwrZt/uAP/oCzZ8/OPOYrX/kK/+bf/BsGgwGdTod/+2//LQD1ep3jx4/zm7/5m0BSBL322mtT57lVSHEjCIIgCIIgCMKYhYUFnnvuOR566CFeffVVTp8+zalTp/iN3/gN7rvvvpnHPPXUU3z1q1/l0Ucf5U//6T/NqVOnaDQaQLL78+u//us8+uijPPjgg+MfJfi5n/s5/s7f+Ts8/vjjt+wHBdT1tpA+D06dOqVPnz79eZshCIIgCIIgCAeat99+m/vvv/+W9tnpdKhWq/R6PX78x3+cX/u1X+OJJ5646X5n2aqUellrfar4XXnnRhAEQRAEQRCEm+YXf/EXeeuttxgMBvz8z//8LSlsPi1S3AiCIAiCIAiCcNP8s3/2zz5vE+SdG0EQBEEQBEEQDgZS3AiCIAiCIAiCcCCQ4kYQBEEQBEEQhAOBFDeCIAiCIAiCIBwIpLgRBEEQBEEQBOFz4Xd+53e49957OXnyJL/8y7980/1JcSMIgiAIgiAIwmdOFEX8pb/0l/j3//7f89Zbb/HP//k/56233rqpPuWnoAVBEARBEARB+FjO7HR5/XKbXhBRtk0eWalxbL5yU32++OKLnDx5krvuuguAn/u5n+O3f/u3eeCBB37oPmXnRhAEQRAEQRCE63Jmp8tLF/bpBREAvSDipQv7nNnp3lS/Fy9eZH19ffz5yJEjXLx48ab6lOJGEARBEARBEITr8vrlNpHWubZIa16/3L6pfnWhTwCl1E31KcWNIAiCIAiCIAjXZbRjc6PtN8qRI0c4f/78+POFCxdYXV29qT6luBEEQRAEQRAE4bqUbfNTtd8oTz31FO+99x4fffQRvu/zL/7Fv+CrX/3qTfUpxY0gCIIgCIIgCNflkZUaZuFxMVMpHlmp3VS/lmXxK7/yK/zxP/7Huf/++/mzf/bP8uCDD95cnzd1tCAIgiAIgiAIB5rRr6Ld6l9LA/ipn/opfuqnfuqm+xkhxY0gCIIgCIIgCB/LsfnKLSlmbjfyWJogCIIgCIIgCAcCKW4EQRAEQRAEQTgQSHEjCIIgCIIgCMKBQIobQRAEQRAEQRAOBFLcCIIgCIIgCIJwIJDiRhAEQRAEQRCEz5y/8Bf+AocOHeKhhx66ZX3e9p+CVkr9CeB/AEzgH2itf/l2n/NWMhgM2PE1m60BWsNq3aNkGewPQy61h1Qdk5WahwK2ej67fZ/Fsst82SaMNZfaQ4ZhzGrdpe5ZtAYhm60hrqVYqXm4hmKrH7DVHdIsOSyVHTRwuT2g40ccrrk0PJtBGLG5PwAFa/USrgV7/YjLnQE112al6qLRbHV99gYBSxWXOc8m0JpLrQFBrFmreVQcg9Yw4lJrgGebrNRcbMNgq+ez1R2yUHZYLDtEWnO5M6TnRxyueTRci24YsdkaYCrFat3DMWN2B5qrnQEN12ap6qKAK50hrWHAoarHnGcwjBSXWgMirVmre5Qdk/1+yKX2gIpjslL1UAZsdX12ej6LFZeFsk2U+m8QxqzWXOqOSTuI2GwNcUzFSj3x33Y/4Fp3SNNzWKo6aK250h7S9kNWqh7NksUgiNlsD9DAWs3Dsw32B0kMa47Jcs3DAK72fPb6PksVl4WSjR9pLrUH+JFmte5SdQ3aw5jN1hDPMhL/qSSG270hcyWHpYpDpOFKJoZzrj32n6EUh+seJVOzM4i50hlQd20Opf672h2yP0j8N+/ZDKOYS+1JDKuOwd4w4nJrQMkxWam6GEqx3ffZ7vosVBwWSg4xmsvtIX0/YqXu0XRNOn7MxfYA21AcrnnYZszeKIaezaGKiwaupjFcrnrMewb9EC61h8Ras1rzqNiK3WHE5faQimOyXHUxFVzrBez2fRbKLosliyBOxlESQ4+GY9AKYjZbAxzT4HDNw1OKq8M0BzyHQxWbWCfjqD3KAdtkEGsutgcwiqGpEj900him/rvWC9gb+GkOWAQaLrcG+FHMat2jZhu0/GQ8eFZigw1cG4RsdYfMlx0WSzZxOpa7fsRKzaXpGPRCuNhOcuBw3cVTsOPHXE1juFxJ8vdaz09imNrgx5rN1pAo1qzWPao27A2TsVVO89BUiq2ez3YvieFi2SaMEy0YBDGH6x51W9ENNRdbwySGdY+aAZcGYZoDNksVF7TmctenPQySHHBNBpFOcmCkY4ZiP4gmOlZ1UWkM90Y6VrISHeukOlbzqNsG7SAZR65lcLjqUjIUV/ohW2kOLJZttIbLneFExxyTfpRoqVKwmsZwdxhxZaRjFQeU4lp3ONaxec8iiGFzpGN1l4oBrYhUxwxWah6Wgu1+wFbXz+tYe0gvSHSs7ip6QeI/y1Cs1l0cQ7M7iLnaHSY6VnHSPPTZH+mYYzDUcKk1THSs5lG2YN/XGR1Lxt9WPxjr2KJnEaR6PsqBupP4b5QDKzWPkoJrw0wM03kgyYFEx+Zci34U53KgZCt2+/kcANhKc2Cx4rLgpvNAe5IDddtgP80B1zI4XHNxleJqP5zoWNlOdCyTA3OuSTdIxpGhFIdrLiWLgo45KNRExyouzTQHLrWGhGkMqw7sDZPcLNmpjhmw3QvGObBQSrTgcntIP0h1zIJORC4HHBN2+on/Jjqmudrxxzo25xkMsjpW96hYyfgr5sBWRscWSiZhTC4Hao5Bp6BjtqHYHuR1bOS/jh+xUnVpOhMdUyQ5UDEV28PJXL5ccZI87BZ0LNWC0VxUS2N46dPqmJvqWGu2jjVcm0NFHat6zLsmw0+pY4sVh0XPJgQupTlwuJbXMcdM1kIlI7E9q2Naa65kdKzhmgx/aB2DS50BwzBmrZbMA3kd83ANuPYJOlZ3Ui3N6pil2B1M69goB0Y65sdM1mN1l6oJ+2HSVrINlmseZqpj22Mds1msep/JevfjCKKYIIqJNdimwjIUpnFr9kd+4Rd+gb/8l/8yf/7P//lb0h+A0lrfss6mOlfKBH4A/DHgAvAS8DWt9Vuzvn/q1Cl9+vTp22bPD8Nmq883P9ph5CUFPHdsnm+d2Rl/p2QZPHN0nt//cGvcdrTpMV+yefVSe9z25fUmb19u0QpiACxD8czROb6Z6Wu+ZPP4ap3f+2B73PbwSo2qbfCd8/sALJWTQuKtq53xdyqOyaMrdZ4/tztuOzFfpu6YvHJ5YsMzR+d48dwuUfrZMRXPbczzBx9OzrdccVipebx2uTVue3K1wRtX2vhRYruh4CvH5vnGRxPba67Fg8s1vpux4f6lKputAfvDcNz2lYL/XMvgwUM1vre5P25bq3scrjmcvjix4akjTd6+2qbjJ9abhuLUWoMXzu/l/LdYcfjBVnfc9uByjSvtAVu9AEhi+MzGHM+fndhZtk2+tN7g6x9O7PrykSYvb+4TxpMcefpokxfP7zFqsg3F46sNXrwwsWGh7PDwco2vfzTx6WOrdd692qEfZvy3Mc83Mn6oOiZfXp/j9z6YjKOTC2X8MObc/mDc9uzGHC+d3SVIPzumwXMbc7kYrlRdlioOb1yZxP6JtQbvXG3TS8ffLF/VXYtTRxr8fmb8/dixeb59dmd8zbNywLMMTq01+dbZSduRhsdS2eaVTA58ab3JG5fa9MMkhpaRjL//mPHVcxtzvLLZohdE47ZHVmp8sN2jm7Yp4OmNOb5TiOHjq3W+nWk7PlcGYj7anfhvKoam4vHD+Rgeqjg8tFzj9z/Mx/D8Xp/tdBwZKvHNf8zkwE+cWOClC/u0M+P97oUKx5oOv/vBxK7nNub47tlJHj56uM7l1oArXX/8nbW6h0JzoTUctz11pMGrmy2C1HhTKb5yLO+/Z4/O8drlFl1/4r8Hl6uc3e2Pc2dWDpQsg3uXqrx6aZJzR5sex+fKuWv88nqTd67usZ+aZRmKr2zM58b7fNnmydU6v/v+pO2RlRqrNZvfeS/p68urVdohUzr2zHqT/5AZfyfmyyyWbF64ONGHZ47O8cK5XeLR9R2qstMPuNSe+Gq56vDISp3ffX+ST0+sNugMfX6w3Qdmx/CZ9TneuNIa+wquo2Mb87nx7loGTxVyYL3hEcWazXY2hk1+sNVhf5D09Wl0rGJqXtxM/KVItDQ7f/yRuxZ49VKL3X4wbjvWLGEZ8P5Of9w2S8eeLsxFi2WHe5YquTHy+GqiIZ+kY08fneM/vJ/VsQpVS/HqlcT29brDUq3E9zIxdUyDZzfm+Hom59bqyWIvq39PrjXoDULe3k58c7Th4VgG72/3xt9puBardY+3r03G1n1LFfp+xNm0r1k54FkG9x+q8srmJAfWGx4PHKrw/3tvYteX1pu8f7XDTjoeTs6XCWLN2b2Jj+dLNvNlO2fXw8s1Yq158+rHx/CVzRZ7g0kMj8+VOTlf4nfTvPAsg4dWapy+MPGfbSoeO9zgpYyOLVcdSrbJmd2JXY+vNnjrSpvhx8zlT6/P8ebVdk7H7l2qcKU9ZG8waXvm6BzfPbc7Xh+5VjIXFeePF87v4keTefTUkQatns8P0jE5S8cansUjK/Wcbx44VKVmwQsfkwNPrtX5aKfPTiEH+kGU09cvrzc5fWGPkVmWoXhircGLmTxcrNg0XJsPdiYxfGSljmNoTm8m89pyxWa+7ObGWsUxeXq9mVvHJesxg1cuJ98rWwb3L9d4uZADj6zUOX1xYsNy1eXxlRrNisvt4O233+b+++//2O8EUUxnGKIB88oH2Ge+hzHsglfFuucprNW7b9qOM2fO8NM//dN8//vf/1S2KqVe1lqfKn73dj+W9iXgfa31h1prH/gXwM/c5nPeUs7tDciWfxr4aKfHH797cdzWD2Pafjh1XM21c23vXutwan1u/DmMNXv9ANeahGGnHzAI49xx71zt5Po6sVjl3cykB9D1I/w4X6h+uNOjUXZybe9tdXlstT7+7EeavUFA1tIrXZ+SY+aOe+tqm/XG5O5BnN7FXKlN+m8PQ6KCDe9udVhr5O86fLDd5am1iQ3DMB4XTSMutgaU7PzG4jvXOjyyMjkuijW7/QDHVOO2nX6AY+aH9bvXOty9WB1/1sC5vT5Nb9J/L4jo+hMbbEOxNwxzhU3SV5eV2uR6gljT9kMyJrDd88eLzxFvXelwpFkaf441XGgNeOLw5Ho6fkSnMI4+2O6x1ijl2t7b6vLMsck48qN4vFAacbkzpOIW/He1w/2HauPPKzWP9wrjqDUMx8UPJIv8i/sDspejgQ+3u/yhjea4bRDG44JlxIX9AdVCDrxztcNjmWsOY812z6eWGW+DMM4VNgBvX837T6f91918DIeF3Dmz2+NwLe+/H2x1x3e4AYJI0/FDjEwMr3b9qXx652qHBzP+i3UyTu9bmvwPzXp+nFsQAHyw0yUqSO372z2e3ZjEsGSZuYkXkr6bpXz+vn01n0+R1lztDHkqm9OxzhU2AO9c63Kkkfff2d0+c6VJfPphPDXez+0NUErl2t691uXpoxP9C2PNdt/nUEZrdnpBbhwBvH2tQ6wnfqiWPN69Nq1jrYLtH+70KBfG8ntbXe5ZnPi97tm5wgbgSscfL8InNrTZmJscN9KxrB6FWucKG0h0bLWoYztdHlqe6MpwRg6c3x8wX9Dgd651ePxwY/x5pGP2DehYvTwZt5pkfD+6MhmTwzDOFTYAZ/b6LBXu/M7Ssf1BQGYqYquXH48Ab15pT+nYxdYgNzd0/Gg6B7a7zGUWZ/cdqvNOpqiFRMdaBR272BpQ96Y15Oj8xIa1RokPMgUEwP4wxDTy4/a9rW7ufz6ogTM7feYzOTAIY4IonwPn9wcUzOLdax2eXG+OPy9V3VxhA0kMPSs/j75zrcNqfeKr0Vz0ZCZ/B2GcK2wgiXOYMeu+pSrvXs3nThAleZ+97Csdn6qTz523r7ZZL8TwUmvIlzI2RFpPxfC9rW7Odkhyc7EyGd/DMD8XGSTrAj+a1tK7FiaxGOnYocokFvuDcGoefXerS62U999HOz2ezsTCMoxcYQNJDixW88VBMQfCWNMa5MfNVjegZBdj2GY+k4d3zVdzNyEg0bH2DB1rlrM5UOOda9M50A8isiP3SmdIt6BjnzVhrMeFjfPe80lhAzDoEH7/m4Sb732u9s3idhc3a8D5zOcLadsYpdQvKqVOK6VOX7t27Tab8+mJ4ulBFcUaVdjximfsgBV3xSLN1EIh0noqCMW+Yq1zBZYC4viTz6dn2qCnthJjDUZ+/piyIdJgFCaLKNbYhb6mbNAjiyeEscYq9DVr/3DKhlhjFPwXz/Bpsa+knxvpa/IdpWbHNIp1rpC5ng2zYlg8XxjrXGE767hZfpkVQ43GLHxvVuyzNih1Hb9nxpZpKKJZftBgmR8f+1ltsdYUd7KjWJPtatZmcmL7tJ3FMVk8dDry6XGzxtGM7xXtLBxGGGuczAXNGjOxnr6mqGB7PDMS07bPGrdRrHML4VlxSK650NeMMflJ42F0nC54K441tvUJORAX+td6tm7G0zkwW8cy/rvOEwhTx8XTcY50Pg9nazmoGTpmGx9/zSP7c9+ZMdhiDQafrGNaz9Bg8+Ntn0U8K580GKqY07OOm/ZDsRCbpWPFllm6MlPHCp8jrafsmnXV0/6b/k6kP1lDkmOntQA1abue12/E9rAQw5k6WrDBULN1Wc+wZLaGFG2IcTOL+NlaPp0DMzUka6dxnXlUa4orq0hrHDMf/en1xPQVhjo/ZmbFeRZFDUmOLSrbLP8V/HydtcIn6ZihmLoZnHxv1hxygxd1m7HPfA8V54s24pDwBy99PgZ9DLe7uCmOE5ia3/Svaa1Paa1PLS0t3WZzPj1Hm6WptuNzZb6eedzCMlTuDjIkd7yLd4BOLpR549JkC1IB8yUnd3ex6phUCncKTixU8P3JnYjze32OzZdz33FMhVdYKK/WXPxCxX9ivswbmcdODAVNz2KYudHR8Cyigu13L1a4mHk0AGC14XE+0+ZZxtQktzFX4konf9xd82VezvjBNNTUImG+bE+J1MmFCm9fnTzipIC5kp27W1+2zamC9Ph8mXOFu2rrjVLuDqdtKKqZ3QM/0jRca2oAn1yo5O4QGyqJWfaOd821pmKR+K9og8d3MlvgjmlQL9xlO9Lw2Orm70ifmC/z4vnJ+DMVNDybrOQ0PZugsBt290KF97Ymd4qudoa5O66QxDDrh0vt4dTOG8DxuRLfzDzCZxmKcmGnbbHsTO0EnFyo8OaVyfhTwFLFYW8wsb5kG1Pj4e6F6fG3VvfYy8ZwRg6sVF12+/k70HctVLjSycew4phkh3zdtSgXdi9PLlSm7hAfaXi8nnn0r+KaUwXresPDLVTEdy2UeenCxH9RpGl4ef/Nl2w6hbundy9Wudia+EEByzWXb2fGkWsZud3M0fk2Czsb680SO5m789aMPDxUcXI7CpDo2NuFGC6UHS5mHp+rOmZuHAGcWChj60m8YmKOzRV1zKBW8MNqzZ3SghPzZd7bmsTCD+PcLhQkOlYp2HD3YiV3zQCH6x7fOrs3/uxaBu4MHbs8Q8e+n9Ej01BUijlQsafugJ9crPDOlI5Z48eEINWxaFrHdJTva2OuzCuZx1rKtjl1zctVl/3CTsCJ+QqXCzrWLNm5HfSaa1EYyty9WOFCQceONLzcYzuOaVAv7NgeaXj0MrvSF/YH3J25cw+JjtXdvI7NeXbuOEjysJW5nq3ukCMzdKy4MD42V+ZKO2/7RrPEdvfjc2Cx7FAuOOLkQoV3MnnfHgQsV/M7dBXHJIyK82+FvX5+HG3MlfhuJn/Ljkm5sAY4XHPxMnn43naXkwX/GSqJfzZXGq7FoLALfs9ihQtFLW14fDPzeJ5tGlM6drRZyukmJGuha5n5yVQqF/swTnZVi8XU3QtV9jJ5qEjG6YWMtpVtc0rPj82ViQqL6+Nz5Zz/FExpz3LVmdrRPLlQ5lJBS+uulZuzqo45NY+eXCzTyyyYLu73b1jHBpmd3fe2u1M5YCjwbDO3SG541tT1fNaMbkarYXf2Fwad2e2fI7f7BwUuAOuZz0eAzdt8zltK07V59ugc72930STiVHMN7lmpc36/T9UxObFQwVaKE/NltvsBy1WXI3UPP4o5XHMZRjHH58oslm0MpQjp4ZoGJxcqeKbi3qUqVzpDFko2G3NlQq1Zb3h0/Ij1RonlmkNnGI1fdN2YK1GykyLoYmtAzTW5a76CqZIJcLcfcLjmslrzGIYxK1WXINbcNV+m6Vnct1zj7G4PzzI4uVjFNTT3LFa42vVZKjscnSsRRsnL//0g4mizxGLVoWKbfLjTwzQUJxcqlC2DBw5VudROXuI8PlcGlTzfuj8MWa17rNVcOkHM+9sdYp0sCOqOxQNLdc7u9Sk7JifnK9iG4uRCma1ewHLF4UjDI4hGgpAsghbLdrJo2+0n31+sUEqfkb7UHjJXsjk+VyLWySNK7WHEkYbHStWl40fjrfET8xWqrsnDHxPDlapLs2TzlWPzvL/dxU9jOFe2eWSlzpm9JIZ3L1RwTMW9ixWudH0WyjYbzTJxJoZHmyUOVRzqrsWHOz0UyQKnbJs8tFxLHr1wLe5KC9bjc2V2BwGrNZfVuscgiGkNI8I0hnOexd2Ldc7t9fEsk5OLFVxDcfdChWu9NIbNUvrS4iSGSxWHsm3ywU4PK/1+yTaouRab7SFzns2xuRKaZNJvDUPW6h4V2xjnQEz67LBrcf9KnXP7fSqOyYn5CrZKFrDboxjWPYJYj3PgWLPMQsnGMhQf7fZwMjlw31KFyx2f+ZJNyTJ47tgcH2z30hzwOFRxmCtNnn0+uVChZhs8vFLjwn6aA3MVLDXx3+Gqy1rdZRBpVvrJIw7H50rMlSweWalxZref5MBCBddgHMPFNIZBmgO9IOJoo8Shis2+bzGIYgw1ssHkweUam60BDdcCnbzz8tFuj/1ByOGay+G6R9uPWa66RGkMG47JPWkMS7ZJ1bU4tdbg3N6Aa73kEa8jTY8w0gSRZhBGbMyVWCxZuFaND3fSHFioUDIV9y9VudRJYlgyDZ7dmOfDnS7tYcRa3WOl4rBccTM6VqZWyIG75ssFHXM4Ui9N65hrYShFN4zHOlYxVfJMfsdPdKxZwo8KOlZ12BmGYx0bhnBirkTFKeiYzsdwte4yjHRGx0o0XZMHV5L3iDzLpOZaPL5a58LegKtpDqw3PYZhIQfKNvvDiMWyM9axqqUyOmbhpu9+fLTTG+vY4apDL4yTHBjpmGvywFI+BxyDnI6t1z38WBNGcapjJRbKNrahCNKd75OLFTxDcd9SlctpDI/PlYiBXpjRsYpDJ0jmAUje86jYBg+kOVB1TGKS90HO7ibvHKxUHdbqHn6U5OFYx7w0B/b6Yx1zjYKONUpEOilMun6aA1WbumvxwU4PI83DsmVM6VisNcfmSuwNwkTHai6DULNcdQljTdW1mHMtLGOSAycWKngmBR3zCCLNMExzoFlisWyxN4xYKDtYhmK5mrzQXR/rmMXxuTKaySNya2kMu0HMoUry7sBd82UabvJex7nRPDCfaMhYx9Ic6If5HJj3bExD0QuTXav5ssPhmsdcqc/lTA7EaHpBNM6BQxWbjp+J4UKFmpXXsTiGp9ebfLTbz+lYN5jkwPG5EvMlC3O1nuZAkoeOCfcsVLjam+hYGOvxo74baQ5URzG8jo55lpHTsdWay0rdYxBEmNsq0bGFRMceWUnncttM8ikzFx0qO5TM5L2s97e7DMKYjbkSS2WL3UESw9Fc7hV07NhcCa2T9/6yOtYL4/EPHpyYL1O1DR7M6FjJMfjSkSZn9/pTOqa1xo+S9cSCZ/HI4Tof7RbXY3kdizX0MzFcrjq0Mjp2pFGibBsZHUtyQOnkJuBu6r9k/ExyYKRjllkf69jJhTJOIQfWGx5z5dvzvs2NYhmKqmMRuRWYVeB41em2z5nb/YMCFskPCvwkcJHkBwX+V1rrN2d9/078QYERfhARaXLvovSCEBuNbSd3KnzfJ1SKsj25czEMQ3Ss8LLvFPgRytC4VvZ9gQBLaxwnEb0gCAjI3w0PohhF/nGgH9aGXhBhKI33MTaEYYivVe4uUt+PMG7IdvI2BCGxVgX/RdjEY9uHwyGRYeSOG4QhUaxydyNv1H8hKvfejh9EaMhtv99MDDGm/WfGMa7rZvyQj2HfT/zu2tnjbsyGOJ7236wYFv0X/9AxzNs+HA4TGzLvgfQGAbYZYtul8XcibVDOPCc/GAwAA89zMm0+Sumxr0Z9WUbWhj5BZOX66vs+Joy/M7GBvP9ilTtuOByitcrZ0B34mMR4npfry1TZGM6woe8n/ivYnrUhCAKCiCkbZvnPsSIsy5v4r5gDgwExZsGnN+K/aRv8IEh1zM4dl43hjfrvxmwYEkTGdAwVOPbNx7A3CDCIPjaGYTjAD80biuEn+e9mciDCoPKp/Tcjhr5PBJSyORAk701+Wv8NBj7cphy4ng2z/DcrhkX/FXPgpmKoVN5/NxDDHz4HpufDHwkdm5EDt0zHZuXALdaxT/TfLYzhjejY7eJGflBgRHDxPaI3vwlxZjfVsLAe+rGb+lGBr33ta3z9619na2uL5eVl/tbf+lv8xb/4F2/I1uv9oMBtLW7SE/8U8N+T/BT0P9Ra/7fX++6dXNwIgiAIgiAIwkHh0xQ3AOHme8k7NoPOLf21tBvh0xQ3t/3/c6O1/nfAv7vd5xEEQRAEQRAE4fZgrd79mRUzN8Pt/kEBQRAEQRAEQRCEzwQpbgRBEARBEARBOBBIcSMIgiAIgiAIP4Lc7nfvbwWf1kYpbgRBEARBEAThRwzP89je3r6jCxytNdvb27lfk/skbvsPCgiCIAiCIAiCcGdx5MgRLly4wLVr1z5vUz4Wz/M4cuTIDX9fihtBEARBEARB+BHDtm2OHz/+eZtxy5HH0gRBEARBEARBOBBIcSMIgiAIgiAIwoFAihtBEARBEARBEA4E6k76hQSl1DXg7Odtx21mEdj6vI04IIgvbw3ix5tHfHjrEF/eGsSPN4f479Yhvrw1iB+n2dBaLxUb76ji5kcBpdRprfWpz9uOg4D48tYgfrx5xIe3DvHlrUH8eHOI/24d4stbg/jxxpHH0gRBEARBEARBOBBIcSMIgiAIgiAIwoFAipvPnl/7vA04QIgvbw3ix5tHfHjrEF/eGsSPN4f479Yhvrw1iB9vEHnnRhAEQRAEQRCEA4Hs3AiCIAiCIAiCcCCQ4uYTUEqtK6X+QCn1tlLqTaXUf5G2zyulflcp9V7637m0fSH9fkcp9SuFvr6ulHpXKfVq+ufQdc75pFLqDaXU+0qpv6eUUmn7LyilrmWO/9/c7uu/VdxhftxQSv2eUur1tK8jt/v6bxW32I+OUurXlFI/UEq9o5T6T69zzuv58ceVUt9TSoVKqZ+93dd+K7nD/PiFzWu443z5I5/bSqlaZiy9qpTaUkr999c554HJ7TvMf5LT3DJf/sjndPpvX0v987pS6neUUovXOeeByembQmstfz7mD3AYeCL9ew34AfAA8H8H/nra/teB/1v69wrwFeA/B36l0NfXgVM3cM4XgWcABfx74H+Ztv9Csc8vyp87zI+/Cfx8+vefAP7Hz9s/n5Mf/xbwf03/bgCLn9KPx4BHgH8K/Ozn7ZsvsB+/sHl9B/pScnu635eBH/+UfvzC5fYd5j/J6Vvnyx/5nAYs4OpID9Pj/5tP6ccvXE7fzB/ZufkEtNaXtNbfS//eBt4G1oCfAf5J+rV/Avyp9DtdrfW3gMEPcz6l1GGgrrX+jk5G5D8d9f1F5g7z4wPA76V//4PUhi8Et9iPfwH479LvxVrrqf852Mf5UWt9Rmv9OhDfsgv8jLiT/PhF5w7zpeR2BqXU3cAh4Jsz/u1A5fad5L8vOneYLyWnk0JFAZV0J6YObBbPd9By+maQ4uZToJQ6BjwOvAAsa60vQTKASZL2RvhH6fbsfz3aLiywBlzIfL6Qto34T9Ntyf+PUmr9U1/EHcAd4MfXgNHjLv8JUFNKLXy6q/j8uRk/KqWa6V//drpV/ZtKqeUZX/2k8fiF5w7x4xc+r+GO8OWPfG4X+BrwP6ULnSIHNrfvEP/9yOd0gR/Wlz/yOa21DoD/HfAGSVHzAPDrM756YHP60yLFzQ2ilKoCvwX8Fa1164fs5s9prR8Gfiz985/NOtWMtpEY/BvgmNb6EeA/MKn8vzDcIX78L4E/pJR6BfhDwEUg/CFt+Vy4BX60gCPAt7XWTwDfAf7urFPNaDswP7F4h/jxC5/XcMf4UnI7z88B//x6p5rR9oXP7TvEf5LT0/ywvvyRz2mllE1S3DwOrAKvA//VrK/OaPvC5/QPgxQ3N0A6sH4L+A2t9b9Mm6+kW4CjrcCrn9SP1vpi+t828M+ALymlzMzLdv8Xkko7+8LcEdLtR631ttZ6mLb/v4Anb/7qPjvuID9uaq3/tNb6ceBvpm37t+QiPwNukR+3gR7wP6effxN44tP48YvOneLHL3pewx3lS8ntSV+PApbW+uX084HP7TvFf5LTU33djC8lp+ExAK31B+nO1/8bePZHIad/WKS4+QTSR55+HXhba/3/yPzTvwZ+Pv37zwO//Qn9WCr9dYt0sP808H2tdaS1fiz9839KtyjbSqmn03P/+VHfo2RI+SrJ85tfCO4wPy4qpUZj/78C/uEtuszbzq3yYyqQ/wb4w2nTTwJvfRo/fpG5k/z4Rc5ruON8+SOf2xm+RuZO+UHP7TvJf5LTU9yMLyWnk92qB5RSS+nnP5b2eaBz+qbQd8CvGtzJf0h+uUKTbAO+mv75KWCB5CW399L/zmeOOQPsAB2SSvoBkl/BeDnt503gfwDM65zzFPB94APgV2D8P1v979JjXyN5se6+z9s/X1A//mx6vh8A/wBwP2//fNZ+TNs3gG+kff0ecPRT+vGptL8uyV33Nz9v/3xB/fiFzes70JeS25N/+/CTxtJByu07zH+S07fOl5LTSft/TlIkv05yE2jhU/rxC5fTN/NndNGCIAiCIAiCIAhfaOSxNEEQBEEQBEEQDgRS3AiCIAiCIAiCcCCQ4kYQBEEQBEEQhAOBFDeCIAiCIAiCIBwIpLgRBEEQBEEQBOFAIMWNIAiCIAiCIAgHAiluBEEQhFuKUuq/UUr9lx/z739KKfXAZ2TLMaXU9z+LcwmCIAifP1LcCIIgCJ81f4rkf8orCIIgCLcUKW4EQRCEm0Yp9TeVUu8qpf4DcG/a9r9VSr2klHpNKfVbSqmyUupZ4KvA31FKvaqUOpH++R2l1MtKqW8qpe77mPNsKKV+Tyn1evrfo2n7P1ZK/T2l1PNKqQ+VUj8749hvKqUey3z+tlLqkVvtC0EQBOHzQ4obQRAE4aZQSj0J/BzwOPCngafSf/qXWuuntNaPAm8Df1Fr/Tzwr4G/prV+TGv9AfBrwP9ea/0k8F8Cv/oxp/sV4J9qrR8BfgP4e5l/Owx8Bfhp4JdnHPsPgF9Ibb4HcLXWr/8QlywIgiDcoUhxIwiCINwsPwb8z1rrnta6RVK8ADyU7pa8Afw54MHigUqpKvAs8JtKqVeB/ydJkXI9ngH+Wfr3/5GkmBnxr7TWsdb6LWB5xrG/Cfy0UsoG/gLwj2/w+gRBEIQvCNbnbYAgCIJwINAz2v4x8Ke01q8ppX4B+MMzvmMAe1rrx27BeYeZv6upL2rdU0r9LvAzwJ8FTv2Q5xQEQRDuUGTnRhAEQbhZvgH8J0qpklKqBvzJtL0GXEp3Sv5c5vvt9N9Id3o+Ukr9GQCV8OjHnOt5kkfgSPv81qe09R+QPMr2ktZ651MeKwiCINzhSHEjCIIg3BRa6+8B/xPwKvBbwDfTf/qvgReA3wXeyRzyL4C/ppR6RSl1gqRI+YtKqdeAN0l2Vq7H/wH4XyulXgf+M+C/+JS2vgy0gH/0aY4TBEEQvhgorWc9SSAIgiAIBw+l1CrwdeA+rXX8OZsjCIIg3GJk50YQBEH4kUAp9edJdpL+phQ2giAIBxPZuREEQRDuOJRSfxP4M4Xm39Ra/7efhz2CIAjCFwMpbgRBEARBEARBOBDIY2mCIAiCIAiCIBwIpLgRBEEQBEEQBOFAIMWNIAiCIAiCIAgHAiluBEEQBEEQBEE4EEhxIwiCIAiCIAjCgeD/Dydb/DHAaCliAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1008x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.show()\n",
    "plt.figure(figsize = (14,6))\n",
    "sns.scatterplot(x='date_only', y = 'week_day', data = df, hue='target',\n",
    "               palette=\"RdBu_r\")\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>text</th>\n",
       "      <th>subject</th>\n",
       "      <th>date</th>\n",
       "      <th>date_only</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>week_day</th>\n",
       "      <th>target</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>As U.S. budget fight looms, Republicans flip t...</td>\n",
       "      <td>WASHINGTON (Reuters) - The head of a conservat...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 31, 2017</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>31</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>U.S. military to accept transgender recruits o...</td>\n",
       "      <td>WASHINGTON (Reuters) - Transgender people will...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 29, 2017</td>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>29</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Senior U.S. Republican senator: 'Let Mr. Muell...</td>\n",
       "      <td>WASHINGTON (Reuters) - The special counsel inv...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 31, 2017</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>31</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>FBI Russia probe helped by Australian diplomat...</td>\n",
       "      <td>WASHINGTON (Reuters) - Trump campaign adviser ...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 30, 2017</td>\n",
       "      <td>2017-12-30</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>30</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Trump wants Postal Service to charge 'much mor...</td>\n",
       "      <td>SEATTLE/WASHINGTON (Reuters) - President Donal...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 29, 2017</td>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>29</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               title  \\\n",
       "0  As U.S. budget fight looms, Republicans flip t...   \n",
       "1  U.S. military to accept transgender recruits o...   \n",
       "2  Senior U.S. Republican senator: 'Let Mr. Muell...   \n",
       "3  FBI Russia probe helped by Australian diplomat...   \n",
       "4  Trump wants Postal Service to charge 'much mor...   \n",
       "\n",
       "                                                text       subject  \\\n",
       "0  WASHINGTON (Reuters) - The head of a conservat...  politicsNews   \n",
       "1  WASHINGTON (Reuters) - Transgender people will...  politicsNews   \n",
       "2  WASHINGTON (Reuters) - The special counsel inv...  politicsNews   \n",
       "3  WASHINGTON (Reuters) - Trump campaign adviser ...  politicsNews   \n",
       "4  SEATTLE/WASHINGTON (Reuters) - President Donal...  politicsNews   \n",
       "\n",
       "                 date  date_only  year  month  day  week_day  target  \n",
       "0  December 31, 2017  2017-12-31  2017     12   31         6       1  \n",
       "1  December 29, 2017  2017-12-29  2017     12   29         4       1  \n",
       "2  December 31, 2017  2017-12-31  2017     12   31         6       1  \n",
       "3  December 30, 2017  2017-12-30  2017     12   30         5       1  \n",
       "4  December 29, 2017  2017-12-29  2017     12   29         4       1  "
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date_only</th>\n",
       "      <th>week_day</th>\n",
       "      <th>target</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-12-30</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   date_only  week_day  target\n",
       "0 2017-12-31         6       1\n",
       "1 2017-12-29         4       1\n",
       "2 2017-12-31         6       1\n",
       "3 2017-12-30         5       1\n",
       "4 2017-12-29         4       1"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['date_only','week_day','target']].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 44888 entries, 0 to 44887\n",
      "Data columns (total 10 columns):\n",
      " #   Column     Non-Null Count  Dtype         \n",
      "---  ------     --------------  -----         \n",
      " 0   title      44888 non-null  object        \n",
      " 1   text       44888 non-null  object        \n",
      " 2   subject    44888 non-null  object        \n",
      " 3   date       44888 non-null  object        \n",
      " 4   date_only  44888 non-null  datetime64[ns]\n",
      " 5   year       44888 non-null  int64         \n",
      " 6   month      44888 non-null  int64         \n",
      " 7   day        44888 non-null  int64         \n",
      " 8   week_day   44888 non-null  int64         \n",
      " 9   target     44888 non-null  int64         \n",
      "dtypes: datetime64[ns](1), int64(5), object(4)\n",
      "memory usage: 3.4+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['title', 'text', 'subject', 'date', 'date_only', 'year', 'month', 'day',\n",
       "       'week_day', 'target'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_date= df[['title','text','subject','date','date_only', 'year', 'month','day','week_day', 'target']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>text</th>\n",
       "      <th>subject</th>\n",
       "      <th>date</th>\n",
       "      <th>date_only</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>week_day</th>\n",
       "      <th>target</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>As U.S. budget fight looms, Republicans flip t...</td>\n",
       "      <td>WASHINGTON (Reuters) - The head of a conservat...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 31, 2017</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>31</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>U.S. military to accept transgender recruits o...</td>\n",
       "      <td>WASHINGTON (Reuters) - Transgender people will...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 29, 2017</td>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>29</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Senior U.S. Republican senator: 'Let Mr. Muell...</td>\n",
       "      <td>WASHINGTON (Reuters) - The special counsel inv...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 31, 2017</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>31</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>FBI Russia probe helped by Australian diplomat...</td>\n",
       "      <td>WASHINGTON (Reuters) - Trump campaign adviser ...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 30, 2017</td>\n",
       "      <td>2017-12-30</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>30</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Trump wants Postal Service to charge 'much mor...</td>\n",
       "      <td>SEATTLE/WASHINGTON (Reuters) - President Donal...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 29, 2017</td>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>29</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               title  \\\n",
       "0  As U.S. budget fight looms, Republicans flip t...   \n",
       "1  U.S. military to accept transgender recruits o...   \n",
       "2  Senior U.S. Republican senator: 'Let Mr. Muell...   \n",
       "3  FBI Russia probe helped by Australian diplomat...   \n",
       "4  Trump wants Postal Service to charge 'much mor...   \n",
       "\n",
       "                                                text       subject  \\\n",
       "0  WASHINGTON (Reuters) - The head of a conservat...  politicsNews   \n",
       "1  WASHINGTON (Reuters) - Transgender people will...  politicsNews   \n",
       "2  WASHINGTON (Reuters) - The special counsel inv...  politicsNews   \n",
       "3  WASHINGTON (Reuters) - Trump campaign adviser ...  politicsNews   \n",
       "4  SEATTLE/WASHINGTON (Reuters) - President Donal...  politicsNews   \n",
       "\n",
       "                 date  date_only  year  month  day  week_day  target  \n",
       "0  December 31, 2017  2017-12-31  2017     12   31         6       1  \n",
       "1  December 29, 2017  2017-12-29  2017     12   29         4       1  \n",
       "2  December 31, 2017  2017-12-31  2017     12   31         6       1  \n",
       "3  December 30, 2017  2017-12-30  2017     12   30         5       1  \n",
       "4  December 29, 2017  2017-12-29  2017     12   29         4       1  "
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_date.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 44888 entries, 0 to 44887\n",
      "Data columns (total 10 columns):\n",
      " #   Column     Non-Null Count  Dtype         \n",
      "---  ------     --------------  -----         \n",
      " 0   title      44888 non-null  object        \n",
      " 1   text       44888 non-null  object        \n",
      " 2   subject    44888 non-null  object        \n",
      " 3   date       44888 non-null  object        \n",
      " 4   date_only  44888 non-null  datetime64[ns]\n",
      " 5   year       44888 non-null  int64         \n",
      " 6   month      44888 non-null  int64         \n",
      " 7   day        44888 non-null  int64         \n",
      " 8   week_day   44888 non-null  int64         \n",
      " 9   target     44888 non-null  int64         \n",
      "dtypes: datetime64[ns](1), int64(5), object(4)\n",
      "memory usage: 3.4+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x7fc17a091cd0>"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 762.375x720 with 20 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(df_date, hue ='target')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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YmKChYUF3vCGN3DHHXdwyy23nPNyV6OsIiIiIiLPF3fn2MKQuWFNFox2boxjDIBAxfplt89cSGZ2t7vvOnX6at4z9TrgncB3zey+ZtoHgduBz5jZe4AngKURGMxsD2mAiZaZvQX4KXe/38z+OfBVMyuBx0kjAmJmt5KC14fd/ftm9hngftJIgu87nyP5nYv3vve93H///fT7fd71rnedlyAlIiIiInKxMzM2ddtsOiUzpbdrdxS/RavWMnUxeL5aplbLxVRWEREREZGL1elaplZ9AAoREREREZEXIoUpERERERGREShMiYiIiIiIjEBhSkREREREZAQKU2vUF7/4RV760pdyzTXXcPvtt1/o4oiIiIiIyCkUptaguq553/vex3/8j/+R+++/n0996lPcf//9F7pYIiIiIiKyzGr+nalLwp5j83znqVkWyprxIuOVl02yc+O5/XGxb37zm1xzzTW8+MUvBuDtb387n//857nhhhvOR5FFREREROQ8UMvUOdhzbJ5v7Z1moUx/G3ihrPnW3mn2HJs/p+Xu27ePK6+8cun9jh072Ldv3zktU0REREREzi+FqXPwnadmqU/5o8e1O995avaclrvSH1I2s3NapoiIiIiInF8KU+dgsUXqTKefqR07dvDkk08uvd+7dy/bt28/p2WKiIiIiMj5pTB1DsaL7Kymn6nXvOY1PPzwwzz22GMMh0M+/elPc+utt57TMkVERERE5PxSmDoHr7xskuyU7neZGa+8bPKclpvnOR/5yEf4+3//73P99dfztre9jRtvvPGclikiIiIiIueXRvM7B4uj9p3v0fwA3vjGN/LGN77xnJcjIiIiIiKrQ2HqHO3c2D0v4UlERERERC4u6uYnIiIiIiIyAoUpERERERGREShMiYiIiIiIjEBhSkREREREZAQKUyIiIiIiIiNQmFqDfv7nf56tW7fy8pe//EIXRURERERETkNhag1697vfzRe/+MULXQwREREREXkW+jtT56ja/zDVD74F/TnoTJBf9xry7dee0zLf8IY3sGfPnvNTQBERERERWRUKU+eg2v8w1ff+FmKVJvTn0ns450AlIiIiIiJrm7r5nYPqB986GaQWxSpNFxERERGRFzSFqXPRnzu76SIiIiIi8oKhMHUuOhNnN11ERERERF4wFKbOQX7dayCccttZyNP0c/COd7yDH/3RH+Whhx5ix44dfOxjHzun5YmIiIiIyPmnASjOweIgE+d7NL9PfepT56N4IiIiIiKyihSmzlG+/VqN3CciIiIicglSNz8REREREZERKEyJiIiIiIiMQGFqBe5+oYvwnC6GMoqIiIiIvJApTJ2i0+lw9OjRNR1W3J2jR4/S6XQudFFERERERC5ZGoDiFDt27GDv3r0cPnz4QhflWXU6HXbs2HGhiyEiIiIicslSmDpFURRcffXVF7oYIiIiIiKyxqmbn4iIiIiIyAgUpkREREREREagMCUiIiIiIjIChSkREREREZERKEyJiIiIiIiMYNXClJldaWZfNrMHzOz7ZvYrzfSNZvYlM3u4ed7QTN/UzD9nZh9ZtpxJM7tv2eOImf2rFda308x6y+b7w9XaNhERERERkdUcGr0CftXd7zGzSeBuM/sS8G7gTne/3cxuA24DfgPoAx8CXt48AHD3WeCmxfdmdjfw56dZ5yPuftNpPhMRERERETlvVq1lyt0PuPs9zetZ4AHgCuDNwMeb2T4OvKWZZ97d7yKFqhWZ2bXAVuBvV6vcIiIiIiIiZ+J5uWfKzHYCNwPfALa5+wFIgYsUjs7UO4A/dXc/zedXm9m9ZvY3Zvb6cymziIiIiIjIs1nNbn4AmNkE8Dng/e4+Y2bnsri3A+88zWcHgKvc/aiZvRr4CzO70d1nTinPe4H3Alx11VXnUhYREREREbmErWrLlJkVpCD1CXdfvM/poJld3nx+OXDoDJf1KiB397tX+tzdB+5+tHl9N/AIcN0K893h7rvcfdeWLVvOeptERERERERgdUfzM+BjwAPu/vvLPvoC8K7m9buAz5/hIt8BfOpZ1rfFzLLm9YuBa4FHz7bcIiIiIiIiZ2I1u/m9jtQl77tmdl8z7YPA7cBnzOw9wBPAWxe/YGZ7gCmgZWZvAX7K3e9vPn4b8MblKzCzW4Fd7v5h4A3AvzCzCqiBX3D3Y6uzaSIiIiIicqmz04/l8MK3a9cu371794UuhoiIiIiIrGFmdre77zp1+vMymp+IiIiIiMgLjcKUiIiIiIjICBSmRERERERERqAwJSIiIiIiMgKFKRERERERkREoTImIiIiIiIxAYUpERERERGQEClMiIiIiIiIjUJgSEREREREZgcKUiIiIiIjICBSmRERERERERqAwJSIiIiIiMgKFKRERERERkREoTImIiIiIiIxAYUpERERERGQEClMiIiIiIiIjUJgSEREREREZgcKUiIiIiIjICBSmRERERERERqAwJSIiIiIiMgKFKRERERERkREoTImIiIiIiIxAYUpERERERGQEClMiIiIiIiIjUJgSEREREREZgcKUiIiIiIjICBSmRERERERERqAwJSIiIiIiMgKFKRERERERkREoTImIiIiIiIxAYUpERERERGQEClMiIiIiIiIjUJgSEREREREZgcKUiIiIiIjICBSmRERERERERqAwJSIiIiIiMgKFKRERERERkREoTImIiIiIiIxAYUpERERERGQEClMiIiIiIiIjUJgSEREREREZQb5aCzazK4E/AS4DInCHu/+BmW0E/hTYCewB3ubux81sE/BnwGuAP3b3X2qWMwn87bJF7wD+H3d//wrr/ADwHqAGftnd/2p1tk5EROTSNjsYMBg6/doZxki3yCiCUUanCBAdYh2pMPIAwQAMSBcfpYHXEDLwmD5xwDHMHMOo3QEIYfGbhrkTY1qUNfNGT5/3a2e8CLg7tcP8sCbPAp3cyM3o1ZFWBkTDLOLNUuu0GoIZhUE/srQtmaWS1TEtM8+MzAwnlcPMqWoosgDuYKmMpafv9qpIJw9kBr2qpnZjvMioo9OvasaKjGFV08ozBsOasVZGwJktI3kw2nnAa8eCMV+m+cuqJs8zqqqmyDIGVdrOPBgxpnn7ZU2nyGgFWKicso508oxWBuZQOiwMa4o80M6MXlXTzjKCQRXBcMCoYtorRRYI5gyr9Dozp4qwUEXGioxBmcrQzgLDOhKaMowVGVV0isyo61Q/wSALUFbpfWap6prdQWZp3+dm1DjBIRpkGN7s72Ht5MEIQLBIIDBbRqI7E60ciHg0hjFSZIHC0rE1iJF+mcqchVQH460MA8o60soDVRXJskCM6bgd1BEzwx1aWSr/MKYCLx7bGcYgetqu2skNanfMQnPkOmXttPIMcAJQOQzLmnaRUcVIFZ12nvZnJ8voVTWdPGuWGRnWTreV0ytrHGjngQDNPk/HcVk7Y3mgbtZpLO7bQCszZvo17TwQcQKp7pfvw3Q8BBynlRtT7fbq/APyArJqYQqogF9193uaQHS3mX0JeDdwp7vfbma3AbcBvwH0gQ8BL28eALj7LHDT4nszuxv481NXZmY3AG8HbgS2A39tZte5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JuxYgGFMXRLbefoRYFin/UFzXOXBmlH4mvEjm8EuspBaSItmBMFhTPMEc3IMzKk81b8bS90C3dOIeRGInn4wMEvd/4zUVbSTh6XuqnlY7NaZylrY4rRUf5087VtI+3mp3jydR046xjHDm9a0QRVTa58ZC01XvhgjIaTWxUF58vjLg5FngRCddQpST2Nmd7v7rlOnr+Zofq8D3gl818zua6Z9ELgd+IyZvQd4AnjrskLuAaaAlpm9Bfgpd7+/+fhtwBuXr8DMbiUFrw+7+/fN7DPA/aSRBN+nkfxERERWz9Qav9haf6ELcIqps5l3bIWJK007A90zmGfDaItm/YhlWg1nsp2XunUrTVxD+/BitGotUxcDtUyJiIiIiMhzOV3LlO4qExERERERGYHClIiIiIiIyAgUpkREREREREagMCUiIiIiIjIChSkREREREZERKEyJiIiIiIiMQGFKRERERERkBApTIiIiIiIiI1CYEhERERERGYHClIiIiIiIyAgUpkREREREREagMCUiIiIiIjIChSkREREREZERKEyJiIiIiIiMQGFKRERERERkBApTIiIiIiIiI1CYEhERERERGYHClIiIiIiIyAgUpkREREREREagMCUiIiIiIjIChSkREREREZERKEyJiIiIiIiMQGFKRERERERkBApTIiIiIiIiI1CYEhERERERGYHClIiIiIiIyAgUpkREREREREagMCUiIiIiIjIChSkREREREZERKEyJiIiIiIiMQGFKRERERERkBApTIiIiIiIiI1CYEhERERERGYHClIiIiIiIyAieNUyZWTCzH3u+CiMiIiIiInKxeNYw5e4R+D+fp7KIiIiIiIhcNM6km9//Z2b/yMxs1UsjIiIiIiJykcjPYJ7/CegClZn1AQPc3adWtWQiIiIiIiJr2HOGKXeffD4KIiIiIiIicjE5k5YpzGwDcC3QWZzm7l9drUKJiIiIiIisdc95z5SZ/ffAV4G/Av558/xbZ/C9K83sy2b2gJl938x+pZm+0cy+ZGYPN88bmumbmvnnzOwjpyyrZWZ3mNkPzOxBM/tHK6xvp5n1zOy+5vGHZ1IBIiIiIiIioziTASh+BXgN8Li7/1fAzcDhM/heBfyqu18PvBZ4n5ndANwG3Onu1wJ3Nu8B+sCHgF9bYVm/CRxy9+uAG4C/Oc06H3H3m5rHL5xB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n3L3+4HfAP6dmf0r4DDwj5v5byUFrw+7+/fN7DPA/aSRBN/3bEFKRJ5f6zrFc88kF5XuRbrsS5nqVUTk/FrVbn5rnVqmRERERETkuZyuZUp3i4qIiIiIiIxAYUpERERERGQEClMiIiIiIiIjUJgSEREREREZgcKUiIiIiIjICBSmRERERERERqAwJSIiIiIiMgKFKRERERERkREoTImIiIiIiIxAYUpERERERGQEClMiIiIiIiIjUJgSEREREREZgcKUiIiIiIjICBSmRERERERERqAwJSIiIiIiMgKFKRERERERkREoTImIiIiIiIxAYUpERERERGQEClMiIiIiIiIjUJgSEREREREZgcKUiIiIiIjICBSmRERERERERqAwJSIiIiIiMgKFKRERERERkREoTImIiIiIiIxAYUpERERERGQEClMiIiIiIiIjUJgSEREREREZgcKUiIiIiIjICBSmRERERERERqAwJSIiIiIiMgKFKRERERERkREoTImIiIiIiIxAYUpERERERGQEClMiIiIiIiIjUJgSEREREREZgcKUiIiIiIjICBSmRERERERERqAwJSIiIiIiMgKFKRERERERkRGsWpgysyvN7Mtm9oCZfd/MfqWZvtHMvmRmDzfPG5rpm5r558zsI6cs6ytm9pCZ3dc8tq6wvp1m1ls2zx+u1raJiIiIiIjkq7jsCvhVd7/HzCaBu83sS8C7gTvd/XYzuw24DfgNoA98CHh58zjVz7n77udY5yPuftP52gAREREREZHTWbWWKXc/4O73NK9ngQeAK4A3Ax9vZvs48JZmnnl3v4sUqkRERERERNa05+WeKTPbCdwMfAPY5u4HIAUu4Bld9k7jj5ruex8yMzvNPFeb2b1m9jdm9vpzLriIiIiIiMhprHqYMrMJ4HPA+919ZsTF/Jy7vwJ4ffN45wrzHACucvebgf8J+KSZTa1Qnvea2W4z23348OERiyMiIiIiIpe6VQ1TZlaQgtQn3P3Pm8kHzezy5vPLgUPPtRx339c8zwKfBH5khXkG7n60eX038Ahw3Qrz3eHuu9x915YtW0bbMBERERERueSt5mh+BnwMeMDdf3/ZR18A3tW8fhfw+edYTm5mm5vXBfAm4HsrzLfFzLLm9YuBa4FHz3U7REREREREVrKao/m9jtQd77tmdl8z7YPA7cBnzOw9wBPAWxe/YGZ7gCmgZWZvAX4KeBz4qyZIZcBfA/+mmf9WYJe7fxh4A/AvzKwCauAX3P3YKm6fiIiIiIhcwszdL3QZLphdu3b57t3PNdq6iIiIiIhcyszsbnffder052U0PxERERERkRcahSkREREREZERKEyJiIiIiIiMQGFKRERERERkBApTIiIiIiIiI1CYEhERERERGYHClIiIiIiIyAgUpkREREREREagMCUiIiIiIjIChSkREREREZERKEyJiIiIiIiMQGFKRERERERkBApTIiIiIiIiI1CYEhERERERGYHClIiIiIiIyAgUpkREREREREagMCUiIiIiIjIChSkREREREZERKEyJiIiIiIiMQGFKRERERERkBApTIiIiIiIiI1CYEhERERERGYHClIiIiIiIyAgUpkREREREREagMCUiIiIiIjIChSkREREREZERKEyJiIiIiIiMQGFKRERERERkBApTIiIiIiIiI1CYEhERERERGYHClIiIiIiIyAgUpkREREREREagMCUiIiIiIjIChSkREREREZERKEyJiIiIiIiMQGFKRERERERkBApTIiIiIiIiI1CYEhERERERGYHClIiIiIiIyAgUpkREREREREagMCUiIiIiIjKCfLUWbGZXAn8CXAZE4A53/wMz2wj8KbAT2AO8zd2Pm9km4M+A1wB/7O6/tGxZXwEuB3rNpJ9y90MrrPMDwHuAGvhld/+r1dm682e632e6H9k/M6CTG9sm2iyUFcMaNo4VZEDLYOjQNug37yucGCNmGcPoFGaAU7uRGxAgc6hxcGN6WNFt5eSWEnQF5AYxQsigjoa7Y9Z8r3mu3JkZ1nRbGUVmzTIBTzsV4ODcgIl2zmQrI7f0eawjWCCYM6hhutenJmNrtwUGGRDdiQ5mRmZpeYOyosLoFhm4Ye54gNohMydzozaY6VdMtNP2QFrn/LCmW2S4O2V0hrXTbWVkBif6FeNF2oa6jlgIGE6/crJgFMHoVzUhBAqD0JQnmDHdrzCDdpZh5hydH9JtFzhOt8jIADfDozOMTqcI1LXjTf1U7rSCkZlRek0VjTwECnNKh4WyJpjRzgKxjmRZSMsMhgFZAHeIi5W+uA+bumt2fZo3g7JK8xrQMqNyluopNt9N3zEcJzSLrZvpGdCP0M2gBPAInvblMBotc2qztM7gWN0cLxhuqRyx2b+Z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\n",
      "text/plain": [
       "<Figure size 1008x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.show()\n",
    "plt.figure(figsize = (14,6))\n",
    "sns.scatterplot(x='date_only', y = 'year', data = df_date, hue='target',\n",
    "               palette=\"RdBu_r\")\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression, LogisticRegression, Lasso, Ridge"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>text</th>\n",
       "      <th>subject</th>\n",
       "      <th>date</th>\n",
       "      <th>date_only</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>week_day</th>\n",
       "      <th>target</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>As U.S. budget fight looms, Republicans flip t...</td>\n",
       "      <td>WASHINGTON (Reuters) - The head of a conservat...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 31, 2017</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>31</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>U.S. military to accept transgender recruits o...</td>\n",
       "      <td>WASHINGTON (Reuters) - Transgender people will...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 29, 2017</td>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>29</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Senior U.S. Republican senator: 'Let Mr. Muell...</td>\n",
       "      <td>WASHINGTON (Reuters) - The special counsel inv...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 31, 2017</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>31</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>FBI Russia probe helped by Australian diplomat...</td>\n",
       "      <td>WASHINGTON (Reuters) - Trump campaign adviser ...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 30, 2017</td>\n",
       "      <td>2017-12-30</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>30</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Trump wants Postal Service to charge 'much mor...</td>\n",
       "      <td>SEATTLE/WASHINGTON (Reuters) - President Donal...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>December 29, 2017</td>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>29</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               title  \\\n",
       "0  As U.S. budget fight looms, Republicans flip t...   \n",
       "1  U.S. military to accept transgender recruits o...   \n",
       "2  Senior U.S. Republican senator: 'Let Mr. Muell...   \n",
       "3  FBI Russia probe helped by Australian diplomat...   \n",
       "4  Trump wants Postal Service to charge 'much mor...   \n",
       "\n",
       "                                                text       subject  \\\n",
       "0  WASHINGTON (Reuters) - The head of a conservat...  politicsNews   \n",
       "1  WASHINGTON (Reuters) - Transgender people will...  politicsNews   \n",
       "2  WASHINGTON (Reuters) - The special counsel inv...  politicsNews   \n",
       "3  WASHINGTON (Reuters) - Trump campaign adviser ...  politicsNews   \n",
       "4  SEATTLE/WASHINGTON (Reuters) - President Donal...  politicsNews   \n",
       "\n",
       "                 date  date_only  year  month  day  week_day  target  \n",
       "0  December 31, 2017  2017-12-31  2017     12   31         6       1  \n",
       "1  December 29, 2017  2017-12-29  2017     12   29         4       1  \n",
       "2  December 31, 2017  2017-12-31  2017     12   31         6       1  \n",
       "3  December 30, 2017  2017-12-30  2017     12   30         5       1  \n",
       "4  December 29, 2017  2017-12-29  2017     12   29         4       1  "
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_date_only = df[['date', 'date_only', 'year', 'month', 'day',\n",
    "       'week_day','target']].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>date_only</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>week_day</th>\n",
       "      <th>target</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>December 31, 2017</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>31</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>December 29, 2017</td>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>29</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>December 31, 2017</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>31</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>December 30, 2017</td>\n",
       "      <td>2017-12-30</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>30</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>December 29, 2017</td>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>29</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44883</th>\n",
       "      <td>January 16, 2016</td>\n",
       "      <td>2016-01-16</td>\n",
       "      <td>2016</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44884</th>\n",
       "      <td>January 16, 2016</td>\n",
       "      <td>2016-01-16</td>\n",
       "      <td>2016</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44885</th>\n",
       "      <td>January 15, 2016</td>\n",
       "      <td>2016-01-15</td>\n",
       "      <td>2016</td>\n",
       "      <td>1</td>\n",
       "      <td>15</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44886</th>\n",
       "      <td>January 14, 2016</td>\n",
       "      <td>2016-01-14</td>\n",
       "      <td>2016</td>\n",
       "      <td>1</td>\n",
       "      <td>14</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44887</th>\n",
       "      <td>January 12, 2016</td>\n",
       "      <td>2016-01-12</td>\n",
       "      <td>2016</td>\n",
       "      <td>1</td>\n",
       "      <td>12</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>44888 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                     date  date_only  year  month  day  week_day  target\n",
       "0      December 31, 2017  2017-12-31  2017     12   31         6       1\n",
       "1      December 29, 2017  2017-12-29  2017     12   29         4       1\n",
       "2      December 31, 2017  2017-12-31  2017     12   31         6       1\n",
       "3      December 30, 2017  2017-12-30  2017     12   30         5       1\n",
       "4      December 29, 2017  2017-12-29  2017     12   29         4       1\n",
       "...                   ...        ...   ...    ...  ...       ...     ...\n",
       "44883    January 16, 2016 2016-01-16  2016      1   16         5       0\n",
       "44884    January 16, 2016 2016-01-16  2016      1   16         5       0\n",
       "44885    January 15, 2016 2016-01-15  2016      1   15         4       0\n",
       "44886    January 14, 2016 2016-01-14  2016      1   14         3       0\n",
       "44887    January 12, 2016 2016-01-12  2016      1   12         1       0\n",
       "\n",
       "[44888 rows x 7 columns]"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_date_only"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Timestamp('2017-12-29 00:00:00')"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_date_only['date_only'][1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df_date_only.iloc[:,2].values\n",
    "y= df['target']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = X.reshape(-1,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.16594149187051244"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = model.fit(X,y)\n",
    "y_pred = model.predict(X)\n",
    "\n",
    "model.score(X,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.63840856, 0.63840856, 0.63840856, ..., 0.29998555, 0.29998555,\n",
       "       0.29998555])"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "lr = LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5228791659240777"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lr = lr.fit(X, y)\n",
    "y_pred = lr.predict(X)\n",
    "lr.score(X,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "ridge = Ridge()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "ridge = ridge.fit(X,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.16594149124026625"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_pred = ridge.predict(X)\n",
    "ridge.score(X,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_true['text_1'] = df_true['text'].str.extract('(-.*)$', expand = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_true['text_1'] = df_true['text_1'].str[2:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The head of a conservative Republican faction in the U.S. Congress, who voted this month for a huge expansion of the national debt to pay for tax cuts, called himself a “fiscal conservative” on Sunday and urged budget restraint in 2018. In keeping with a sharp pivot under way among Republicans, U.S. Representative Mark Meadows, speaking on CBS’ “Face the Nation,” drew a hard line on federal spending, which lawmakers are bracing to do battle over in January. When they return from the holidays on Wednesday, lawmakers will begin trying to pass a federal budget in a fight likely to be linked to other issues, such as immigration policy, even as the November congressional election campaigns approach in which Republicans will seek to keep control of Congress. President Donald Trump and his Republicans want a big budget increase in military spending, while Democrats also want proportional increases for non-defense “discretionary” spending on programs that support education, scientific research, infrastructure, public health and environmental protection. “The (Trump) administration has already been willing to say: ‘We’re going to increase non-defense discretionary spending ... by about 7 percent,’” Meadows, chairman of the small but influential House Freedom Caucus, said on the program. “Now, Democrats are saying that’s not enough, we need to give the government a pay raise of 10 to 11 percent. For a fiscal conservative, I don’t see where the rationale is. ... Eventually you run out of other people’s money,” he said. Meadows was among Republicans who voted in late December for their party’s debt-financed tax overhaul, which is expected to balloon the federal budget deficit and add about $1.5 trillion over 10 years to the $20 trillion national debt. “It’s interesting to hear Mark talk about fiscal responsibility,” Democratic U.S. Representative Joseph Crowley said on CBS. Crowley said the Republican tax bill would require the  United States to borrow $1.5 trillion, to be paid off by future generations, to finance tax cuts for corporations and the rich. “This is one of the least ... fiscally responsible bills we’ve ever seen passed in the history of the House of Representatives. I think we’re going to be paying for this for many, many years to come,” Crowley said. Republicans insist the tax package, the biggest U.S. tax overhaul in more than 30 years,  will boost the economy and job growth. House Speaker Paul Ryan, who also supported the tax bill, recently went further than Meadows, making clear in a radio interview that welfare or “entitlement reform,” as the party often calls it, would be a top Republican priority in 2018. In Republican parlance, “entitlement” programs mean food stamps, housing assistance, Medicare and Medicaid health insurance for the elderly, poor and disabled, as well as other programs created by Washington to assist the needy. Democrats seized on Ryan’s early December remarks, saying they showed Republicans would try to pay for their tax overhaul by seeking spending cuts for social programs. But the goals of House Republicans may have to take a back seat to the Senate, where the votes of some Democrats will be needed to approve a budget and prevent a government shutdown. Democrats will use their leverage in the Senate, which Republicans narrowly control, to defend both discretionary non-defense programs and social spending, while tackling the issue of the “Dreamers,” people brought illegally to the country as children. Trump in September put a March 2018 expiration date on the Deferred Action for Childhood Arrivals, or DACA, program, which protects the young immigrants from deportation and provides them with work permits. The president has said in recent Twitter messages he wants funding for his proposed Mexican border wall and other immigration law changes in exchange for agreeing to help the Dreamers. Representative Debbie Dingell told CBS she did not favor linking that issue to other policy objectives, such as wall funding. “We need to do DACA clean,” she said.  On Wednesday, Trump aides will meet with congressional leaders to discuss those issues. That will be followed by a weekend of strategy sessions for Trump and Republican leaders on Jan. 6 and 7, the White House said. Trump was also scheduled to meet on Sunday with Florida Republican Governor Rick Scott, who wants more emergency aid. The House has passed an $81 billion aid package after hurricanes in Florida, Texas and Puerto Rico, and wildfires in California. The package far exceeded the $44 billion requested by the Trump administration. The Senate has not yet voted on the aid. '"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_true['text_1'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(21417, 11)"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_true.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>text</th>\n",
       "      <th>subject</th>\n",
       "      <th>date</th>\n",
       "      <th>date_only</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>week_day</th>\n",
       "      <th>target</th>\n",
       "      <th>text_1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>8247</th>\n",
       "      <td>Obama drinks coconut water to cool down in Laos</td>\n",
       "      <td>U.S. President Barack Obama visited a street m...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>September 7, 2016</td>\n",
       "      <td>2016-09-07</td>\n",
       "      <td>2016</td>\n",
       "      <td>9</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8970</th>\n",
       "      <td>Graphic: Supreme Court roundup</td>\n",
       "      <td></td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>June 16, 2016</td>\n",
       "      <td>2016-06-16</td>\n",
       "      <td>2016</td>\n",
       "      <td>6</td>\n",
       "      <td>16</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                title  \\\n",
       "8247  Obama drinks coconut water to cool down in Laos   \n",
       "8970                   Graphic: Supreme Court roundup   \n",
       "\n",
       "                                                   text       subject  \\\n",
       "8247  U.S. President Barack Obama visited a street m...  politicsNews   \n",
       "8970                                                     politicsNews   \n",
       "\n",
       "                    date  date_only  year  month  day  week_day  target text_1  \n",
       "8247  September 7, 2016  2016-09-07  2016      9    7         2       1    NaN  \n",
       "8970      June 16, 2016  2016-06-16  2016      6   16         3       1    NaN  "
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_true[df_true['text_1'].isna()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'U.S. President Barack\\xa0Obama\\xa0visited a street market in Luang Prabang on Wednesday (September 7), where he greeted residents and tasted fresh\\xa0coconut. He walked near the river of Mekong where women sell\\xa0coconut\\xa0drinks and tasted the local refreshment, posing for photographs and conversing with locals. Obama\\xa0arrived in Laos Tuesday morning (September 6), becoming the first sitting U.S. president to visit landlocked Laos, where the United States waged a “secret war” while fighting in Vietnam, dropping an estimated two million tonnes of bombs on the country. Obama’s visit follows his attendance at the G20 summit in the Chinese city of Hangzhou. He is also due to attend an annual international gathering in the Southeast Asian region.'"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_true['text'][8247]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "#let's drop the empty strings rows\n",
    "\n",
    "df_true = df_true[df_true.text !=' ']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>text</th>\n",
       "      <th>subject</th>\n",
       "      <th>date</th>\n",
       "      <th>date_only</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>week_day</th>\n",
       "      <th>target</th>\n",
       "      <th>text_1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>8247</th>\n",
       "      <td>Obama drinks coconut water to cool down in Laos</td>\n",
       "      <td>U.S. President Barack Obama visited a street m...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>September 7, 2016</td>\n",
       "      <td>2016-09-07</td>\n",
       "      <td>2016</td>\n",
       "      <td>9</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                title  \\\n",
       "8247  Obama drinks coconut water to cool down in Laos   \n",
       "\n",
       "                                                   text       subject  \\\n",
       "8247  U.S. President Barack Obama visited a street m...  politicsNews   \n",
       "\n",
       "                    date  date_only  year  month  day  week_day  target text_1  \n",
       "8247  September 7, 2016  2016-09-07  2016      9    7         2       1    NaN  "
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_true[df_true['text_1'].isna()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_true = df_true.dropna()\n",
    "df_true = df_true.reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(21415, 11)"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_true.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "df_fake = df_fake.drop(['date'], axis=1)\n",
    "df_true = df_true.drop(['text','date'], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_true = df_true.rename(columns ={\"text_1\":\"text\"})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>subject</th>\n",
       "      <th>date_only</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>week_day</th>\n",
       "      <th>target</th>\n",
       "      <th>text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>As U.S. budget fight looms, Republicans flip t...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>31</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>The head of a conservative Republican faction ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>U.S. military to accept transgender recruits o...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>29</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>Transgender people will be allowed for the fir...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Senior U.S. Republican senator: 'Let Mr. Muell...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>31</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>The special counsel investigation of links bet...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>FBI Russia probe helped by Australian diplomat...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>2017-12-30</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>30</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>Trump campaign adviser George Papadopoulos tol...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Trump wants Postal Service to charge 'much mor...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>29</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>President Donald Trump called on the U.S. Post...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               title       subject  date_only  \\\n",
       "0  As U.S. budget fight looms, Republicans flip t...  politicsNews 2017-12-31   \n",
       "1  U.S. military to accept transgender recruits o...  politicsNews 2017-12-29   \n",
       "2  Senior U.S. Republican senator: 'Let Mr. Muell...  politicsNews 2017-12-31   \n",
       "3  FBI Russia probe helped by Australian diplomat...  politicsNews 2017-12-30   \n",
       "4  Trump wants Postal Service to charge 'much mor...  politicsNews 2017-12-29   \n",
       "\n",
       "   year  month  day  week_day  target  \\\n",
       "0  2017     12   31         6       1   \n",
       "1  2017     12   29         4       1   \n",
       "2  2017     12   31         6       1   \n",
       "3  2017     12   30         5       1   \n",
       "4  2017     12   29         4       1   \n",
       "\n",
       "                                                text  \n",
       "0  The head of a conservative Republican faction ...  \n",
       "1  Transgender people will be allowed for the fir...  \n",
       "2  The special counsel investigation of links bet...  \n",
       "3  Trump campaign adviser George Papadopoulos tol...  \n",
       "4  President Donald Trump called on the U.S. Post...  "
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_true.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_fake = df_fake[['title', 'subject', 'date_only', 'text']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>subject</th>\n",
       "      <th>date_only</th>\n",
       "      <th>text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Donald Trump Sends Out Embarrassing New Year’...</td>\n",
       "      <td>News</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>Donald Trump just couldn t wish all Americans ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Drunk Bragging Trump Staffer Started Russian ...</td>\n",
       "      <td>News</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>House Intelligence Committee Chairman Devin Nu...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Sheriff David Clarke Becomes An Internet Joke...</td>\n",
       "      <td>News</td>\n",
       "      <td>2017-12-30</td>\n",
       "      <td>On Friday, it was revealed that former Milwauk...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Trump Is So Obsessed He Even Has Obama’s Name...</td>\n",
       "      <td>News</td>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>On Christmas day, Donald Trump announced that ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Pope Francis Just Called Out Donald Trump Dur...</td>\n",
       "      <td>News</td>\n",
       "      <td>2017-12-25</td>\n",
       "      <td>Pope Francis used his annual Christmas Day mes...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               title subject  date_only  \\\n",
       "0   Donald Trump Sends Out Embarrassing New Year’...    News 2017-12-31   \n",
       "1   Drunk Bragging Trump Staffer Started Russian ...    News 2017-12-31   \n",
       "2   Sheriff David Clarke Becomes An Internet Joke...    News 2017-12-30   \n",
       "3   Trump Is So Obsessed He Even Has Obama’s Name...    News 2017-12-29   \n",
       "4   Pope Francis Just Called Out Donald Trump Dur...    News 2017-12-25   \n",
       "\n",
       "                                                text  \n",
       "0  Donald Trump just couldn t wish all Americans ...  \n",
       "1  House Intelligence Committee Chairman Devin Nu...  \n",
       "2  On Friday, it was revealed that former Milwauk...  \n",
       "3  On Christmas day, Donald Trump announced that ...  \n",
       "4  Pope Francis used his annual Christmas Day mes...  "
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_fake.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_true['target'] = 'real'\n",
    "df_fake['target'] ='fake'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>subject</th>\n",
       "      <th>date_only</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>week_day</th>\n",
       "      <th>target</th>\n",
       "      <th>text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>As U.S. budget fight looms, Republicans flip t...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>31</td>\n",
       "      <td>6</td>\n",
       "      <td>real</td>\n",
       "      <td>The head of a conservative Republican faction ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>U.S. military to accept transgender recruits o...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>29</td>\n",
       "      <td>4</td>\n",
       "      <td>real</td>\n",
       "      <td>Transgender people will be allowed for the fir...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Senior U.S. Republican senator: 'Let Mr. Muell...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>2017-12-31</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>31</td>\n",
       "      <td>6</td>\n",
       "      <td>real</td>\n",
       "      <td>The special counsel investigation of links bet...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>FBI Russia probe helped by Australian diplomat...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>2017-12-30</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>30</td>\n",
       "      <td>5</td>\n",
       "      <td>real</td>\n",
       "      <td>Trump campaign adviser George Papadopoulos tol...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Trump wants Postal Service to charge 'much mor...</td>\n",
       "      <td>politicsNews</td>\n",
       "      <td>2017-12-29</td>\n",
       "      <td>2017</td>\n",
       "      <td>12</td>\n",
       "      <td>29</td>\n",
       "      <td>4</td>\n",
       "      <td>real</td>\n",
       "      <td>President Donald Trump called on the U.S. Post...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               title       subject  date_only  \\\n",
       "0  As U.S. budget fight looms, Republicans flip t...  politicsNews 2017-12-31   \n",
       "1  U.S. military to accept transgender recruits o...  politicsNews 2017-12-29   \n",
       "2  Senior U.S. Republican senator: 'Let Mr. Muell...  politicsNews 2017-12-31   \n",
       "3  FBI Russia probe helped by Australian diplomat...  politicsNews 2017-12-30   \n",
       "4  Trump wants Postal Service to charge 'much mor...  politicsNews 2017-12-29   \n",
       "\n",
       "   year  month  day  week_day target  \\\n",
       "0  2017     12   31         6   real   \n",
       "1  2017     12   29         4   real   \n",
       "2  2017     12   31         6   real   \n",
       "3  2017     12   30         5   real   \n",
       "4  2017     12   29         4   real   \n",
       "\n",
       "                                                text  \n",
       "0  The head of a conservative Republican faction ...  \n",
       "1  Transgender people will be allowed for the fir...  \n",
       "2  The special counsel investigation of links bet...  \n",
       "3  Trump campaign adviser George Papadopoulos tol...  \n",
       "4  President Donald Trump called on the U.S. Post...  "
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_true.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "combined_df = [df_true, df_fake]\n",
    "df = pd.concat(combined_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Resetting the index since combining 2 df creates duplicate indexes\n",
    "df.reset_index(drop=True, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "fake    0.522902\n",
       "real    0.477098\n",
       "Name: target, dtype: float64"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Mostly positive reviews but date is pretty evenly distributed\n",
    "\n",
    "df.target.value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package stopwords to\n",
      "[nltk_data]     /Users/unachka/nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n"
     ]
    }
   ],
   "source": [
    "import nltk\n",
    "nltk.download('stopwords')\n",
    "from nltk.corpus import stopwords"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "stop_words = stopwords.words('english')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "alphanumeric = lambda x: re.sub('\\w*\\d\\w*', ' ', x)\n",
    "punc_lower = lambda x: re.sub('[%s]' % re.escape(string.punctuation), ' ', x.lower())\n",
    "spelling = lambda x: re.sub(\"(.)\\\\1{2,}\", \"\\\\1\", x)\n",
    "\n",
    "df['text'] = df.text.map(alphanumeric).map(punc_lower).map(spelling)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'president donald trump called on the u s  postal service on friday to charge “much more” to ship packages for amazon  amzn o picking another fight wit'"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['text'][4][:150]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "#R Remove stop words\n",
    "df['text'] = df['text'].apply(lambda x: \" \".join(x for x in x.split() if x not in stop_words))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Vectorization and Topic Modeling "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.decomposition import TruncatedSVD, NMF\n",
    "from sklearn.metrics import pairwise_distances\n",
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "from sklearn.manifold import TSNE\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>aa</th>\n",
       "      <th>aab</th>\n",
       "      <th>aaba</th>\n",
       "      <th>aabo</th>\n",
       "      <th>aaccording</th>\n",
       "      <th>aachen</th>\n",
       "      <th>aadhaar</th>\n",
       "      <th>aadhar</th>\n",
       "      <th>aadl</th>\n",
       "      <th>aaf</th>\n",
       "      <th>...</th>\n",
       "      <th>zyklon</th>\n",
       "      <th>zynga</th>\n",
       "      <th>zypries</th>\n",
       "      <th>zyries</th>\n",
       "      <th>zyuganov</th>\n",
       "      <th>zz</th>\n",
       "      <th>zzbluecomet</th>\n",
       "      <th>zzjjpdaivn</th>\n",
       "      <th>zztaine</th>\n",
       "      <th>émigré</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44881</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44882</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44883</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44884</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44885</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>44886 rows × 105169 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       aa  aab  aaba  aabo  aaccording  aachen  aadhaar  aadhar  aadl  aaf  \\\n",
       "0       0    0     0     0           0       0        0       0     0    0   \n",
       "1       0    0     0     0           0       0        0       0     0    0   \n",
       "2       0    0     0     0           0       0        0       0     0    0   \n",
       "3       0    0     0     0           0       0        0       0     0    0   \n",
       "4       0    0     0     0           0       0        0       0     0    0   \n",
       "...    ..  ...   ...   ...         ...     ...      ...     ...   ...  ...   \n",
       "44881   0    0     0     0           0       0        0       0     0    0   \n",
       "44882   0    0     0     0           0       0        0       0     0    0   \n",
       "44883   0    0     0     0           0       0        0       0     0    0   \n",
       "44884   0    0     0     0           0       0        0       0     0    0   \n",
       "44885   0    0     0     0           0       0        0       0     0    0   \n",
       "\n",
       "       ...  zyklon  zynga  zypries  zyries  zyuganov  zz  zzbluecomet  \\\n",
       "0      ...       0      0        0       0         0   0            0   \n",
       "1      ...       0      0        0       0         0   0            0   \n",
       "2      ...       0      0        0       0         0   0            0   \n",
       "3      ...       0      0        0       0         0   0            0   \n",
       "4      ...       0      0        0       0         0   0            0   \n",
       "...    ...     ...    ...      ...     ...       ...  ..          ...   \n",
       "44881  ...       0      0        0       0         0   0            0   \n",
       "44882  ...       0      0        0       0         0   0            0   \n",
       "44883  ...       0      0        0       0         0   0            0   \n",
       "44884  ...       0      0        0       0         0   0            0   \n",
       "44885  ...       0      0        0       0         0   0            0   \n",
       "\n",
       "       zzjjpdaivn  zztaine  émigré  \n",
       "0               0        0       0  \n",
       "1               0        0       0  \n",
       "2               0        0       0  \n",
       "3               0        0       0  \n",
       "4               0        0       0  \n",
       "...           ...      ...     ...  \n",
       "44881           0        0       0  \n",
       "44882           0        0       0  \n",
       "44883           0        0       0  \n",
       "44884           0        0       0  \n",
       "44885           0        0       0  \n",
       "\n",
       "[44886 rows x 105169 columns]"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cv = CountVectorizer()\n",
    "doc_word = cv.fit_transform(df[\"text\"])\n",
    "pd.DataFrame(doc_word.toarray(), columns=cv.get_feature_names())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Over 100K Unique words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "def vectorize(data, vectorizer, binary):\n",
    "    if vectorizer == \"cv\":\n",
    "        if binary == True:\n",
    "            vec = CountVectorizer(stop_words, ngram_range=(1, 3), binary=True)\n",
    "        else:\n",
    "            vec = CountVectorizer(stop_words, ngram_range=(1, 3))\n",
    "    elif vectorizer == \"tfidf\":\n",
    "        vec = TfidfVectorizer(stop_words, ngram_range=(1, 3))\n",
    "\n",
    "    doc_word = vec.fit_transform(data)\n",
    "    feature_names = vec.get_feature_names()\n",
    "    id2word = dict((v, k) for k, v in vec.vocabulary_.items())\n",
    "    \n",
    "    return doc_word, feature_names, id2word"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "def lsa(doc_word, feature_names, num_topics):\n",
    "    model = TruncatedSVD(num_topics)\n",
    "    doc_topic = model.fit_transform(doc_word)\n",
    "    for ix, topic in enumerate(model.components_):\n",
    "        print(\"\\nTopic \", ix)\n",
    "        print(\", \".join([feature_names[i] for i in topic.argsort()[:-21:-1]]))\n",
    "\n",
    "def nmf(doc_word, feature_names, num_topics):\n",
    "    model = NMF(num_topics)\n",
    "    doc_topic = model.fit_transform(doc_word)\n",
    "    for ix, topic in enumerate(model.components_):\n",
    "        print(\"\\nTopic \", ix)\n",
    "        print(\", \".join([feature_names[i] for i in topic.argsort()[:-21:-1]]))\n",
    "\n",
    "def lda(doc_word, feature_names, id2word, num_topics):\n",
    "    corpus = matutils.Sparse2Corpus(doc_word.transpose())\n",
    "    model = models.LdaModel(corpus=corpus, num_topics=num_topics, id2word=id2word, passes=5, random_state=42)\n",
    "    topics = model.print_topics()\n",
    "    for n, topic in topics:\n",
    "        print(\"\\nTopic \", n)\n",
    "        print(topic)\n",
    "\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/anaconda3/lib/python3.8/site-packages/sklearn/utils/validation.py:70: FutureWarning:\n",
      "\n",
      "Pass input=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', \"you're\", \"you've\", \"you'll\", \"you'd\", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', \"she's\", 'her', 'hers', 'herself', 'it', \"it's\", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', \"that'll\", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', \"don't\", 'should', \"should've\", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', \"aren't\", 'couldn', \"couldn't\", 'didn', \"didn't\", 'doesn', \"doesn't\", 'hadn', \"hadn't\", 'hasn', \"hasn't\", 'haven', \"haven't\", 'isn', \"isn't\", 'ma', 'mightn', \"mightn't\", 'mustn', \"mustn't\", 'needn', \"needn't\", 'shan', \"shan't\", 'shouldn', \"shouldn't\", 'wasn', \"wasn't\", 'weren', \"weren't\", 'won', \"won't\", 'wouldn', \"wouldn't\"] as keyword args. From version 1.0 (renaming of 0.25) passing these as positional arguments will result in an error\n",
      "\n"
     ]
    }
   ],
   "source": [
    "doc_word, feature_names, id2word = vectorize(df, \"cv\", False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Topic  0\n",
      "text, subject, year, month, date_only, day, week_day, target, title\n",
      "\n",
      "Topic  1\n",
      "subject, week_day, target, date_only, year, title, text, day, month\n",
      "\n",
      "Topic  2\n",
      "date_only, year, week_day, title, text, target, subject, month, day\n",
      "\n",
      "Topic  3\n",
      "target, text, title, subject, date_only, day, week_day, month, year\n"
     ]
    }
   ],
   "source": [
    "lsa(doc_word, feature_names, 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Topic  0\n",
      "date_only, year, week_day, title, text, target, subject, month, day\n",
      "\n",
      "Topic  1\n",
      "day, title, subject, year, week_day, text, target, month, date_only\n",
      "\n",
      "Topic  2\n",
      "subject, target, week_day, year, title, text, month, day, date_only\n",
      "\n",
      "Topic  3\n",
      "year, month, week_day, title, text, target, subject, day, date_only\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/anaconda3/lib/python3.8/site-packages/sklearn/decomposition/_nmf.py:312: FutureWarning:\n",
      "\n",
      "The 'init' value, when 'init=None' and n_components is less than n_samples and n_features, will be changed from 'nndsvd' to 'nndsvda' in 1.1 (renaming of 0.26).\n",
      "\n"
     ]
    }
   ],
   "source": [
    "nmf(doc_word, feature_names, 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "def vectorize(data, vectorizer, binary):\n",
    "    if vectorizer == \"cv\":\n",
    "        if binary == True:\n",
    "            vec = CountVectorizer(stop_words, ngram_range=(1, 3), binary=True)\n",
    "        else:\n",
    "            vec = CountVectorizer(stop_words, ngram_range=(1, 3))\n",
    "    elif vectorizer == \"tfidf\":\n",
    "        vec = TfidfVectorizer(stop_words, ngram_range=(1, 3))\n",
    "\n",
    "    doc_word = vec.fit_transform(data)\n",
    "    feature_names = vec.get_feature_names()\n",
    "    id2word = dict((v, k) for k, v in vec.vocabulary_.items())\n",
    "    \n",
    "    return doc_word, feature_names, id2word"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [],
   "source": [
    "def lsa(doc_word, feature_names, num_topics):\n",
    "    model = TruncatedSVD(num_topics)\n",
    "    doc_topic = model.fit_transform(doc_word)\n",
    "    for ix, topic in enumerate(model.components_):\n",
    "        print(\"\\nTopic \", ix)\n",
    "        print(\", \".join([feature_names[i] for i in topic.argsort()[:-21:-1]]))\n",
    "\n",
    "def nmf(doc_word, feature_names, num_topics):\n",
    "    model = NMF(num_topics)\n",
    "    doc_topic = model.fit_transform(doc_word)\n",
    "    for ix, topic in enumerate(model.components_):\n",
    "        print(\"\\nTopic \", ix)\n",
    "        print(\", \".join([feature_names[i] for i in topic.argsort()[:-21:-1]]))\n",
    "\n",
    "def lda(doc_word, feature_names, id2word, num_topics):\n",
    "    corpus = matutils.Sparse2Corpus(doc_word.transpose())\n",
    "    model = models.LdaModel(corpus=corpus, num_topics=num_topics, id2word=id2word, passes=5, random_state=42)\n",
    "    topics = model.print_topics()\n",
    "    for n, topic in topics:\n",
    "        print(\"\\nTopic \", n)\n",
    "        print(topic)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/anaconda3/lib/python3.8/site-packages/sklearn/utils/validation.py:70: FutureWarning:\n",
      "\n",
      "Pass input=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', \"you're\", \"you've\", \"you'll\", \"you'd\", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', \"she's\", 'her', 'hers', 'herself', 'it', \"it's\", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', \"that'll\", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', \"don't\", 'should', \"should've\", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', \"aren't\", 'couldn', \"couldn't\", 'didn', \"didn't\", 'doesn', \"doesn't\", 'hadn', \"hadn't\", 'hasn', \"hasn't\", 'haven', \"haven't\", 'isn', \"isn't\", 'ma', 'mightn', \"mightn't\", 'mustn', \"mustn't\", 'needn', \"needn't\", 'shan', \"shan't\", 'shouldn', \"shouldn't\", 'wasn', \"wasn't\", 'weren', \"weren't\", 'won', \"won't\", 'wouldn', \"wouldn't\"] as keyword args. From version 1.0 (renaming of 0.25) passing these as positional arguments will result in an error\n",
      "\n"
     ]
    }
   ],
   "source": [
    "doc_word, feature_names, id2word = vectorize(df, \"cv\", False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Topic  0\n",
      "text, week_day, subject, title, year, day, date_only, month, target\n",
      "\n",
      "Topic  1\n",
      "text, month, date_only, target, week_day, year, title, subject, day\n",
      "\n",
      "Topic  2\n",
      "subject, month, day, text, year, date_only, title, target, week_day\n",
      "\n",
      "Topic  3\n",
      "target, title, text, subject, month, date_only, day, week_day, year\n"
     ]
    }
   ],
   "source": [
    "lsa(doc_word, feature_names, 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Topic  0\n",
      "text, month, title, day, year, week_day, target, subject, date_only\n",
      "\n",
      "Topic  1\n",
      "day, week_day, year, title, text, target, subject, month, date_only\n",
      "\n",
      "Topic  2\n",
      "subject, year, week_day, text, title, target, month, day, date_only\n",
      "\n",
      "Topic  3\n",
      "target, month, year, week_day, title, text, subject, day, date_only\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/anaconda3/lib/python3.8/site-packages/sklearn/decomposition/_nmf.py:312: FutureWarning:\n",
      "\n",
      "The 'init' value, when 'init=None' and n_components is less than n_samples and n_features, will be changed from 'nndsvd' to 'nndsvda' in 1.1 (renaming of 0.26).\n",
      "\n"
     ]
    }
   ],
   "source": [
    "nmf(doc_word, feature_names, 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [],
   "source": [
    "def display_cluster(X,km=[],num_clusters=0):\n",
    "    alpha = 0.5\n",
    "    s = 20\n",
    "    color=[\"orange\", \"yellow\", \"yellowgreen\", \"forestgreen\", \"skyblue\", \"royalblue\", \"darkorchid\", \"violet\", \"deeppink\"]\n",
    "    if num_clusters == 0:\n",
    "        plt.scatter(X[:,0], X[:,1], alpha=alpha, s=s, c=color[6]) \n",
    "    else:\n",
    "        for i in range(num_clusters):\n",
    "            plt.scatter(X[km.labels_==i,0], X[km.labels_==i,1],alpha=alpha, s=s, c=color[i])\n",
    "            plt.scatter(km.cluster_centers_[i][0], km.cluster_centers_[i][1], marker='x', s=100, c=color[i])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "display_cluster(doc_topic)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
