# Quiz

1. How much programming or coding would be ideal in a position for you?

   a. 75% of the week

   b. 50% of the week

   c. 25% of the week

   d. 100% of the week

1. Which of these best describes you?

   a. I prefer to code on my own

   b. I prefer to code by collaboration, primarily online (GitHub pull requests, VSCode LiveShare, Slack etc.)

   c. I prefer to code by collaboration, primarily in-person i.e. a co-located team but online when necessary

   d. I prefer to code with supervision or assistance

1. Which of these styles of work dynamic best describe your ideal relationship with how you receive software engineering work?

   a. I prefer if requirements and expectations are clearly defined, assigned, and executed.

   b. I am comfortable if objectives and outcomes are loosely outlined with overall less structure. Naturally, this would require me to additionally follow-up with customers and other team members to help define the requirements.

   c. I am passionate about being involved (possibly as the principal maintainer or product owner) to shape the design, direction, and objectives under the guidance of the company's set target results.

   d. I look to fundamentally understand why particular problems are worth solving and generally need to believe in the value proposition that such solutions will have to the customer. Ultimately, I'd prefer to help define the company's target results.

1. What is wrong with the following quote?

   > <pre>Being busy does not always mean real work. The object of all work is production or accomplishment and to either of these ends there must be forethought, system, planning, intelligence, and honest purpose, as well as perspiration.  Seeming to do is not doing.</pre>
   >
   > ― <cite>Thomas A. Edison</cite>

1. Please read this question in its entirety before beginning the problem.

   **Setup**: This problem will focus on an open-source framework that our company primarily maintains: [DataJoint](https://pypi.org/project/datajoint/). Please review the relevant [docs](https://docs.datajoint.io/python/) and [tutorials](https://tutorials.datajoint.io/), setup a user account with [DataJointIO](https://datajoint.io/), and utilize the [Playground](https://playground.datajoint.io/) to quickly get setup for this exercise. Ultimately, you will be connecting to our tutorial database: `tutorial-db.datajoint.io`.

   **Context**: Consider an experiment where the subjects are [Shot Put](https://www.worldathletics.org/disciplines/throws/shot-put) athletes where for each session they make an attempt to send a weight as far as possible i.e as a projectile. There are various weights composed of different materials and each subject may make one attempt during a session. The objective of the experiment is to compare actual recorded data with derived classical physics based models to identify correlation.

   The following is a simplified DataJoint workflow to capture session data and generate computed results for comparison.

   ![nothing](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASUAAADrCAYAAAAv8oAHAAAABmJLR0QA/wD/AP+gvaeTAAAgAElEQVR4nO3deXxU1d3H8c9syWyZ7CRAyAIJS0CysgiyFBFF6g5qxRZRXKtW6GJbW5e2Wq1dHm2Vap+6Vm3FnYoKPiCbQoAAsiRkgSTEkJB1sk8ymXn+uMlIFkiAmcwk+b195RUz9869Z+6Qb845c+45KqfT6UQIIXzDGrW3SyCEEKeSUBJC+BQJJSGET9F6uwBiaGullQYavF2MASeIIG8XwWOGbCjZbDZqa2u9XQyvsFgs+Pv7e7sYADTQwF720kSTt4syYAQTzIVc6O1ieMyQDSW73U5Dw9D8C200Gn0mlACaaGIEI7xdjAGhjjrs2L1dDI+SPiUhhE+RUBJC+BQJJSGET5FQEkL4FAklIYRPkVASQvgUCSUhhE+RUBJC+BQJJSGET5FQEkL4FAklIYRPkVASQviUIXtDrhjYMrIzeH396+Qcz6G6vhqL0UJibCLLFy4nJT7lrI41d+Vcls5fyu2Lbj+vfYR7SE1JDDhbv97KXX++C4vRwpN3PsmaR9fwxO1P4HQ6ufNPd5JVmOX2cz78g4e5OOVitx7zP5v+w8MvP+zWYw4GEkp9sGjRIv7xj390euyxxx7jO9/5TqfH8vPziYuLo7Ky8rTHKi4uJi4ujra2tjOes7y8nLi4OBobG8+94IPUh9s/JCYiht/d9jtS4lOIiYhh6vip/OWHf2H25NkUnSxy+znnpcxj9IjRbj2mJ8JzMJBQ6oOZM2eyc+fOTo/t3LmT2tpaysrKXI9lZGQwbtw4QkNDT3us4cOHk5GRgUajOa8y3XLLLRQWFp7XMQayAGMAKpWq02NajZY/3v1HLp1yqeuxGffO4LXPXuu032OvPsZNv7up02MOh4On3nqKuQ/M5cIfXsiq51dhrbe6ts9dOZd/fPyPTvuv/mg1l//8cqbePZUrfnkFb/7fm52OaW+z85d3/sIlP7mEafdMY/Eji3lv63sArHh6BR9u/5C1X64l5fYUjhw/cn4XZBCRUOqDmTNnsmvXLhwOBwBWq5WysjLmzZtHRkaGa7+dO3cyc+bMMx5Lo9EQHh5+3mXKyck572MMVAumLODA0QM89dZTlFaVuuWY7299H3+dPy8/+DJP3fkUmTmZPP7G46fdf/VHq/nX+n/xwOIHWPfkOu668i6eefcZ1nyxxrXPH/79B9btWMevf/Br3nn0HW6afxNPvfkUW7/eyuqVq5kUN4lF0xex8/mdjI0a65bXMRhIKPXBlClTaGxsJDs7G1BqRMnJySQnJ3eqQZ0aSnv37uXaa69l3rx5XHbZZXzwwQdA9+bb22+/zZw5c7jkkkt4+umnWbp0Ke+++67rmBs2bODSSy8lOTmZlStX4nA4uPfeezlx4gS33HILH3/8cX9dBp+xIH0Bv/7Br9m0dxMLH1zI1b+6mt+9/ju2fL0Fh9NxTse0mCw8sPgB4obHMXvybJbOX8qmvZtobmnutm+jrZE3Pn+DH1z6AxakLyAsMIxF0xdx1cyreG29Uiurb6rng20fcNeVdzF78mxGDRvFtbOuZefqncyaPAudVocKFWq1Gj+dX7da31AmodQHRqORlJQUduzYASjhM2XKFKZMmeKqKR0/fpzy8nKmTZtGbW0tt956K3fffTcbN27kxRdf5NFHH+XIkc5V9NLSUh566CH++te/smHDBqKioti9e3enpl12djaffvopn3/+OZs2beKrr77imWeeAeCVV15h0aJF/XQVfMu1s65l3VPreOOhN7hm1jV8U/ENK59byQ2P3UBJZclZHy81IbXTz2NHjcXeZud4+fFu+xaVFdFkayJ9XHq3YxSXF1NdV03O8Rxa7a2Mjx5/1mUZ6iSU+ujUfqWOUEpISKCiooKqqipX7clkMrF9+3aCg4O55JJLAIiOjmb+/PndajUZGRmMHj2ayZMnA3DjjTei0+k67bNs2TJUKhVhYWGMGTOGkpKz/4UbrNQqNYmxiSy7dBmrV67mvd+8R21DLU//++mzPlagObDTzwZ/AwDNtu41pQprBaD0C6XcnuL6+sU/fgFAdV019c31AOj99GddlqFOxin10cyZM3n11Vepr6/n6NGjTJ48GZVKRWpqKhkZGWRkZDBjxgxA+eTsm2++4aKLLup0jMsvv7zTz9XV1QQHB7t+VqlUjBw5stM+FovF9f9qtdrVrzWUOZ1OnE4nanXnv6kxETHMTprN5v2bXY+p6N4sarJ1XzmlvrG+x32MemO3fU0GEwCrV67usSZkMVqoqa8B6NRZLvpGQqmPUlJSsNlsfPTRRyQlJblqNFOnTiUzM5Pdu3fzxBNPABAREUFsbCyfffZZt+MUFxe7/t9isWC1dv5HKzWhM6uqq+Kqh65ixaIVLLt0WadtTqeTnOIcggO+DfoAYwC1jd8upeVwODhUcIgAY0Cn5x4qONTp59ziXPy0fowKH9WtDGOjxuKn9aOwrJDpidN7LGdCVAJajZbM3ExSx6b2uI/omTTf+kij0TBt2jRef/11pk6d6np8ypQpbNu2jdLSUlJTlX98M2bMoLy8nE2bNgHKp3VLliwhMzOz0zFTU1PJzc11daC//fbbvY5fAqVGpdFougXaUBASEMJlUy/j2fee5U9v/4mMrAyyirLY8vUWVj2/igNHD3Drwltd+0+MncinGZ+SVZhFQWkBj//r8e6dyk4oqSzhlU9f4WTNSXZl7+LN/3uTS9IvwU/n160MJr2JJXOX8MLaF9i0dxOV1kqOHD/Cfc/e5xoMGWAM4IoZV/DqZ6/y+Z7POXbiGB99+RHT75nOup3rlH1MAeQcz+HYiWOdgnOok5rSWZgxYwaPP/44v/71r12PXXDBBRQUFJCenu6qPQUEBPDPf/6T3/72tzz22GM4nU4WL15MSkoK33zzjeu5MTExPPjggyxfvpygoCAWLVrEuHHjei2HWq3miiuu4Oabb+bHP/4xy5Yt6/U5g8kvl/6SCTETWPvlWj7e8TH1TfWEBYYxIXoCL/3sJZLjk137rlyyksdefYxb/3ArZoOZpfOXEhoY2qmJZ2+zc9ui2yipKOH6R6/H1mrjogsu4sHvPXjaMqxasgqzwczT/3mak9UnCTIHMT1xOvddc59rn5/f9HNMehNPvvkkdY11DA8dzg+v/iGXT1Oa8TddfBMP/fMhlv9hOb9f8XsunDh4F5g8Gyqn0+n0diG8oaGhgfLycm8Xo5t58+bx8MMPM3fuXI+dIzw8HJPJ5LHjn40aaviSL31+Mco5P5rDDy79AbddfptXy1FHHQCzmOXVcnjQGqkp9cHevXs5ceKE24/b0tLC3/72N66++mpGjx5NTk4OJSUllJWVsW7duj4fJzU1lcjISLeXT0BDcwNHio5Q11RHWGCYt4szJEgo9cGePXu69Qe5i9lsZvXq1TgcDnQ6HZMmTWLz5s29P/EUw4cPHzKh9My7z/Tr+fJL8tl+cDvDgoaRW5zrsfP/6LofeeS4A5GEUh+sWLHC20UQ7SwmS+87uVFKQgopCWc3FYo4PxJKYkBZftlybxdBeJgMCRBC+BQJJSGET5FQEkL4FAklIYRPkVASQvgUCSUhhE+RUBJC+BQJJSGET5FQEkL4FAklIYRPkVASQvgUCSUhhE+RUBJC+BQJJSGET5FQEkL4FJlPaQhpaWnBz6/76hy+oITuS0u1NLfgp/fN8nqLHTvBBPe+4wA2ZEPJZDJ5fPL82tpajh07RlJSkkfP0xctLS3s3r2b0aNH+8yiAQA6dCSS2OmxNnsb+UfyUbepGT/Z+8te25pt5BzM4YL0C7xdlCFhyIZSf7BarT4TAH5+fiQnJ3Pw4EFqa2tJSEjovv6ZF5ja/+tQV1fH4cOHiQ2OJX5CPGof6GFw+DkoaywjxhnjE9dssPP+Oz6I1dTUEBgY2PuO/cRoNJKWlkZLSwv79++npaXF20XqpLi4mK+//prRo0czduzYbstye4tarUan0/nc9RqsfONdH6Rqa2t9KpRAWel30qRJhISEkJmZSV1dnbeLRGtrKwcOHODkyZOkpaURHh7u7SJ1o9fraW5u9nYxhgQJJQ9paGhAp9P5bMdydHQ0o0eP5uuvv6asrMxr5aipqWH37t0YDAZSUlLQ6/VeK8uZSCj1H+lT8hBfa7r1ZNiwYRiNRg4dOkRDQwNxcXH92mdSVFREcXEx48ePJyQkpN/Oey70ej1NTU3eLsaQIDUlD7FarT4fSqAshpmamkpdXR0HDhzAbrd7/JwtLS18/fXXVFVVkZaW5vOBBEoo2Ww2bxdjSJBQ8pDW1laCgoK8XYw+0el0TJ48GbPZzJ49e2hoaPDYuaqrq9mzZw8Wi4WkpCT8/f09di53kppS/5Hmm4f4wtiks6FSqVxjmPbv38/YsWMJCwtz2/GdTieFhYWUlpaSmJg4IGqRp5I+pf4joSQ6iYiIwGQyucYzuaOfqbm5maysLNRqNampqT7b+X8mer2elpYWnE6njFXyMGm+iW7MZjNpaWnU1tZy8ODB8+pnqqioIDMzk+DgYCZPnjwgAwmUmqSfn5/0K/UDCSXRI51OR1JSEgaDgczMTBobG8/q+Q6Hg7y8PPLy8pg0aRKxsbEDvoYhTbj+IaEkTkulUhEfH09UVBR79+6loqKiT89rbGwkMzOT5uZm0tPTsVgsHi5p/5BQ6h/SpyR6NWLECEwmE4cPH6axsZHo6OjT7lteXk5ubi7R0dFERUX1Yyk9T0Kpf0hNSfRJYGAgqampVFRUcPjwYdra2jpt72iuHTt2jMmTJw+6QAIJpf4ioeRmJ0+exOFweLsYHuHv709ycjIajYa9e/e6fkEbGxvZs2cPra2tpKWlYTabvVxSz5CxSv1Dmm9uZLfbycnJ8ckbSt1FrVYzbtw4SkpKyMzMJDQ0lMrKSsaMGUNERIS3i+dRUlPqH1JTciOr1UpAQMCA/5SpL4YNG4ZGo2H79u2EhIQM+kACpabY2to6aGvCvkJCyY0Gyv1u56uurs51q8iNN95IQ0MDWVlZg/6XVcYq9Q8JJTeyWq0D5n63c9UxEVtcXBwTJkzAaDSSkpIC0KmfabAyGAyD/jV6m4SSmzgcDurr6wkICPB2UTyiYyK2srIyUlNTGTZsmGubWq1mwoQJhIeHk5mZSU1NjRdL6lnSr+R50tHtJrW1tZhMJjQajbeL4na1tbUcPnyYsLAwJk6ceNppaqOjozGbzRw+fJi4uDiGDx/ezyX1PAklz5OakpsM1qZbcXExBw8eJCEhgfj4+F7nzQ4JCSElJYXi4mJycnIGXT+ThJLnSSi5SVBQ0KD6BKpjIraKigrS0tIIDQ3t83MNBgOpqak+u0DB+ZBQ8jwJJTcJDAz0meWUzlfHRGxms/mcJ2LrWKAgNDSUPXv2UFtb64GS9j8ZQOl50qckXDomYispKXHbvNnR0dGu+ZlGjx5NZGSkG0rqPX5+ftjtdhwOh88sATXYyFUVANhsNvbt24fVaiU9Pd2t82aHhoaSnJxMUVEROTk5OJ1Otx27v6lUKvz9/aUJ50ESSoKKigr27Nnj0YnYjEYjqamp2Gy2Ad/PJP1KniWhNIQ5nU6OHj1KXl4eEydO9PhEbFqtlkmTJmGxWHxmIcxzIQMoPUv6lIao5uZmDh8+jJ+fH+np6Wi1/fNPoWOBArPZzIEDB0hISBhwNzBLTcmzJJSGIF+YiK1jIcyDBw9SV1fX7wthng+9Xt/nWTjF2ZPm23nKy8ujurra28XoE1+biK1jgYL+XAjTHaSm5FkSSuepoqICvV7v7WL0qmPebF+biK0/F8J0Fwklz5Lm23mw2Ww4HA4MBoO3i3JGpaWl5OfnExMT4/XaUU88vRCmu/n5+dHW1kZbW9ugvNfR2ySUzkNNTY1Pz5/U1tZGTk4O9fX1JCcn+/yI84iICIxGI4cOHXLbQpie0jFWydev6UAkzbfz4Ms34dbV1bF7924AUlNTB8wvT0BAgNsWwvQkacJ5joTSefDVmlJJSUmnidgGWhOjo5/Jz8/vnBbC7A8SSp4joXSOWltbaWlp8akaiN1u59ChQ5w4caLbRGwDTccCBVFRUezbt8/nPuGUUPIc6VM6R/X19QQGBvpMn0dtbS1ZWVmEhoYyYcKEQXOz6KkLYY4cOfKMC2H2J4PBMGBHpPs6CaVzFBwc7DP9ScXFxRQVFTFu3LizmvdooOhYCPPQoUPU19czbtw4rzdJpabkOYPjz6mXeLuW1Nraes4TsQ00HQthqtVqn1igQELJcySUBqiamhp2796N0Wg854nYBhq1Ws348eMZMWIEmZmZXu1n0ul0OBwOn/10cCCT5tsA44mJ2AaaESNGYDQaOXz4MFFRUV7rZ+qoLfnK6PjBQmpKA4gnJ2IbaIKCgkhNTaW8vNxrC2FKE84zJJQGiOrqajIzMz06EdtAo9frSU5OxuFwsG/fvn6fOE5CyTMklHyc0+mkoKCAI0eOkJiY6PGJ2AYajUbDxIkTCQsL6/cFCiSUPEP6lM6SzWajra0No9Ho8XOdOhFbWloaOp3O4+ccqDoWwjx48GC/LYSp1+uxWq0eP89Q47VQaqCBcsq9dfpz1tDSQFNjE2FGz97F3mZvY1/mPkbGjCRkZAjf8E2P+8US69FyDCQdC2F2TByXkJDg0VqlTIvrGV4LpVZaOcxhb53+3AUoXyc56dnzaEE3RUeVrooqqrpttmMnmGAJpS46FsLMyspi3759TJw40WP9b9J88wyvN99GMMLbRfBdZ2it1SG3OJxOx0KYRUVFZGZmMnHiRAICAtx+no55ze12e7/NcT4USEe3GLSio6NJSEjgwIEDlJaWeuQcsmKu+0koiUEtNDSUpKQkCgsLPbIQpjTh3E9CSQx6JpOJ1NRUmpqa3L5AgYSS+0koiSHB7QsUOJ3Q3IzJ4cBZXQ0VFVBeDpWVUF0N9fXQ2uqewg8x0jsnhoxTF8Lcv3//uS2E2dgIdXVK8DQ3M7ytTXm8sBC6Dj/Q6cBohOBgMJtBRuH3iYSSGHLOaSHMhgalNlRVpdSS9HoICIAzzevU0qI8r6YG/P0hPBxCQpSwEqclzTcxJJ26EOYZFyiw26GkBHJzlUAKCFCCxWg8cyCBUjOyWCA0VNn3+HHlODU1SrCJHkkoiSGro5/JZDL1vEBBc7PSLCsp+bYZdq7jkQwGCAsDhwOOHoUTJ5T/F91IKIkhraOfKSYmhn379lFRUaFsaGyEggKorVVqOu7qDzKbldpWSYlSc+rokxIu0qckBMpCmHq9nsOHD6Ox2wmuqYGmJqV25G46nXLc8nJQq2HkSOW7AKSmJIRLYGAgaUlJBNXXey6QOmg0yvHLypRwEi4SSkKcwq+mBlVNDfTHSjUazbdNOVmuyWXANd8ysjN4ff3r5BzPobq+GovRQmJsIssXLiclPqVfyzJ35VyWzl/K7Ytu79fzCg9paICTJ5VPzPprIj1/f6VWVloKJpM04xhgobT166386G8/YuHUhTx555OEBIRQVl3G6+tf584/3cmrP3+VCTET+q08D//gYWIjYvvtfANBeVYWuZ98Qu3x49jq6tAZjQTHxTF20SJCx4517ffxvfcyZsECxl95pUfLc1bnqahQPqp3U6f2/vffpyI/n4t/8hPXY+V5eeR+8QW1J05ga2hAp9cTHBXF2LQ0QsPCPNtk7KK/3oOzNaBC6cPtHxITEcPvbvuda7BbTEQMqQmp/PzFn1N0sqhfQ2leyrx+O9dAULp/Pzv+53+Imj6dKXffjb/FQlN1NbmffMK2P/yBOb/6FUGxsQCkLF9OQD/MDtlnjY2ucUhHt2+npriY1BtucOspSrOy2PHSS0SlpDDl5pvxN5tpslrJ/eILtv3rX8wJDiZozpx+q6X53HvQbkCFEkCAMaDb6FutRssf7/5jp8ccDgcv/PcF1n65lgprBRHBEXzv4u9x08U3ufbJzM3kufefI6c4B4fDQUJUAvdcfQ9Tx0/t0/auzbcWewvPffAcn2V8RmVtJWGBYSyctpB7rroHrUa51Bevupg7r7wTa72V/2z6D80tzaSOTeWRZY8QahnYi0kWbtmCKSKCtDvucL1H5shIwsaOJeP556kvK3OF0oi0NC+WtAd1dUotSaulprjYI6cozMjAFBZG2ve+9+31CQ8nLC6OjNdeo/74cYIaG5VmXD/wufeg3YAKpQVTFvDgCw/y1FtPsezSZUSGRJ5239UfrebNz9/kkVseITUhlZ1ZO/nNa79Bp9GxZO4SmmxN3P/X+7niwit4fMXjALz9xdvc9+x9fPaHz/DX+Z9xe5C5e0foE/96gi/2fcFjyx9jUuwk9uXv45FXHqGltYWf3KBU4bUaLe988Q6zkmbxz5/9k0prJatWr+LFtS/yi6W/8MBV60cqFX4mU7c/GiqNhmn33dfpsa5Nh3X338+4K6+kqaKCY5s3o1KrSbj0UsYsWMDel1+mdN8+dCYTE665hphZswBYe+edjL/6ahIWLnQdN/Oll7AWFfGdRx/tsYhNVVUceOstKo4cobWxEWNYGGPmz2d0VBTo9WxdvZqK/HwACnftYt6qVVgiI8nesIHC3bux1dVhCAxk9EUXEd9eDoDm2loy336birw8tHo9sdOm9Xx9jMaer8/y5UpNraEBTCacDgfZH35I4bZt2KxWDCEhjJ4/n/gFC1zPq8zJ4dA772A9fhycTixRUSRedx3hEyb0aXvX98Bht3P43Xcp3rmTZqsVQ1AQUdOnk3jttajaR6+vu/9+xl91Fa0NDeR//jltLS2EjRtH6m234W+x9HjNz9bACqX0BdQ31fPi2hf598Z/ExMRQ/q4dGYnzeaiCy5CrVI6CRttjbzx+Rssu3QZC9KVN3HR9EXsz9/Pa+tfY8ncJRSXF9PQ1MAl6Ze4wu3ea+7l8mmXY9KbKCgtOOP2rmrqa1j71VruveZe5iTNAeDi1Is5cPQAb3/xNj+67kfotMo9Twa9gfuuUX5JYyJimDN5DocKDnn24vWDqKlTyXj+efb/618kLFyI8SyWEVdrNBzbuJGY2bP5zqOPUvDFFxx+7z0qc3OJmj6dCddey5GPPmL/a68xPDUVv3OsTex77TVsViszf/pT/EwminfuZP+rr2L87neJTE9n5h13sOW55zCHh5OyZAlqjYasTz8lf9s2Uq+/ntC4OMpzc9m7Zg0ajYa4GTMA2P3WWzRUVnLR3Xejt1jI37aNb/bvx/+UhSqjkpLIeP119n/wAQlz5mDs2n+k0yk1tmHDyHr/ffI3bCD11lsJHTuW8sOH2fvyy2i0WuLmzcNus/HVX/7CqJkzSb/zTgCObdzIV3/+M5f++c9o/PzOuN2/h5k49736KiWZmaTffjtBcXFU5eWR+b//S1trK5Nvuunb92nTJoYnJzP7l7+k2Wpl51//SvaHH5L0/e+f03vS1YAKJYBrZ13L1RddTXZhNruO7GLH4R2sfG4lo4eP5pn7nmFE6AiKyoposjWRPi6903NTE1JZ88UaquuqiYmMISYihl/+45csmbuEGZNmMH7UeOJHxgP0ur2rjiZe0uikTo9PjJ1Ik62JopNFjBkxBoAL4i7otE+gKZDaxv5bGshTRk6dSkpTE9kffsjRzz9Xmm7jxzM8OZnIpKRe+0r0gYEkXHYZAAmXX07uJ5+gDwoieuZMAOIvvZSi7dupLy0lZMyYcyrjhQ880OnnhIULObpuHWU5OUROm4YaZZS3Wq1Go9Vit9nI37qV+LlzGZmkvLej0tKoLCwkd/Nm4mbMoMlqpTw3l9TrryckJgaASd/9LiUHDnS+PklJpDQ3k71hA0e3bVOabmPGMDwxkcgJE5QO9uZm7A0N5K9fT/zChYycqnQVjJoxg8q8PHI//ZS4efNoOHmS1qYmoqZOdYX/xMWLGXXhhegMBupOnDjj9q5sdXUUbd9O4nXXEZmcDCjNu6q8PI5t3Mik669H3X6LjVavJ3HxYkBpnkcmJ1N99Og5vR89GXChBKBWqUmMTSQxNpFlly6jsKyQO/54B0//+2n+8sO/UGFVbhVY8fSKHp9fXVdNcEAwLz/4Mq989grvbXmPv73/NyJDIrn/2vtZOG0hflq/M27vqqFJmZ8nwNT5L1CAUfm5sfnb+6oM/l3+Uahw+4yI3hI7Zw6xs2dTXVBARXY2Jw8eZMezzxIwYgQXPvAAxrDTrwITeMry237tNYyeHmvteo/aedJbLLSc5pj1FRXYW1oI7xKCYXFxHPvyS1oaGqgrKwPAckqnsUqlInjUKNe2DrHTphE7dSrVxcVU5OdzMieHHa+8QkBEBBcuW4ZRq6W+pAS7zUb4+PGdzzl2LMc2bqSlro6A4cMxR0ay6+9/J+473yFi8mQCo6OxREUB9Lq9q9riYpwOByHxnf/oBo8eTe4nn1BfVoZl5EjXY6fyN5upcuN7MqBCyel04nQ6UXcZyxETEcPspNls3r8ZAJNBqdqvXrma8dHjux3HYlTavsEBwaxcvJKVi1dSUFrAa+tf46F/PkTc8DjGR4/vdfupzAblF6auofMgOGuDtdP2IUGlIjgujuC4OBIWLqS+tJRtTz3FgTffZNr995/2aZpTPorv6HfRuHkOoupjx8j+8ENqCgpobWjA6XDgaGzE2N4B35WtfVDj1tWre95eX4/dZgNA26WsOr2+50K0B1bwqFEkzJ1LfXk52/7+dw6sXcu0q6/GVlOjnPPJJ09bJr+AAOY89BA569ZRsHkzh999F2NoKBOXLCFq+nTUWu0Zt3dlb59nvGuzWNe+vqH9lNk1tf7+nfZx4t4/qgMmlKrqqrjqoatYsWgFyy5d1mmb0+kkpziH4ACljT42aix+Wj8KywqZntj9DQAorymnoLSAKeOnABAbGcuvvv8r1n65ltziXEItoWfc3jWUxkWPQ6vRsj9/P6ljU12PHzh6ALPBTHRENIOd0+kEpxNVlz8aHVX8E3v3uveEPTQH29oDoietDexcQJoAABL3SURBVA18+cc/EjZuHLN+8QuMoaGotVo2//znp31Oxy/gzDvuILC9pnAqP4OBpvYFKe1dlg1v6bKgwGmvT3g4kYmJnDh0CJxOV7jN/OlPO9UUXedsDw6/gAAm3XADk264gfrSUnI/+YTdL7yAefhwgmJiet3e6XW2N+lauszI2VJfD9Bjk89TBszw0ZCAEC6behnPvvcsf3r7T2RkZZBVlMWWr7ew6vlVHDh6gFsX3gqASW9iydwlvLD2BTbt3USltZIjx49w37P38fDLDwNw9MRR7v7L3fxn0384UXmCksoSXvnkFQAuGH1Br9u7shgtXDXzKl5d/yrbDmyj0lrJZ7s+472t77F0/lI06l7m3hngbLW1/Peee8j77LNu25xOJ9bjx/Fz8zJHOqOxU1PO6XBQdYa+jZrCQloaGkhcvBhzRARqrZbWhgZqS0tP298VOGIEaq2W+vJy/E2mbl8qtZqA9tkra0+c6FyWggLXz7b6ev7761+Tt2VLt3M4nU6sJ07gZzSCSkVgdLRyztJS/AMCun2p1Gqaa2ooz8pyHcMcGUnKLbeAWo31+PFet3d7ndHRqDQaqvLyOj1elZ+P1mDAFBFx2uvqbgOmpgTwy6W/ZELMBNZ+uZaPd3xMfVM9YYFhTIiewEs/e4nk+GTXvquWrMJsMPP0f57mZPVJgsxBTE+c7vrUa9qEaTyy7BHe+PwNnnn3GdRqNWNGjOF/7v0fYiNjiY2MPeP2njz4vQcxG8z85rXfUFVbRWRIJCsuX8Hyhcv74/J4lb/Fwqjp0zm0Zg3NNTVEJiWhM5lorq6mcMsWqvPzSb/rLreeMzgujuIdOxiRlobG35+8Tz/t1rQ/lSE0FJVKxfEdOxgzfz71ZWUcWbuWoOhoGisqcDqdqFQqdHo9Nd98Q11ZGf4BAcRdeCFZ69djCAwkOCYGW10dh9atQx8QQOoNN2AIDiYkNpbsDRswhoTgbzaTv3Wr62N0UPpdRqWkcGjdOppra4mcMAGd0Uiz1UphRgbVhYWk33gjaDRoTSbi5s0j64MPMAQHEzxmDDarlUPvvIPeYiF1xQpqv/mGr/78Zy646SaGJyfjdDo5vmMHAKHx8b1u78rPZCJm1ixyP/mEwFGjCIyJoSI7m8LNm0lYuBB1bxPauZHK6aUe1hpq+JIvZTHKc9SxGOUsZvWyZ/9xOp0UbtlC0bZt1JWWYm9qwj8wkODYWOIvu4zQhATXvl3HyHy6ciXRF11E4nXXufZ5/5ZbSFm+nNg5yhCLpqoqPl21ihk//jERF1xAw8mTZL70EtVHj6IzGolfsIDW5mZO7N3Lxb/9bY/nOfr55+R8/DEt9fUExsSQdPPN2EpL2fWnP2GIiODin/yEsuxsdr/1FgBTli4lPD6eI59/TsGuXdhqa9EZDAwbN45Jixahbx+b01hdTebbb1N57Bg6vZ7Y6dNRqVQU79vHJQ8++O31ycigaNcu6srLsdts+AcEEBwVRfycOYRGRCgDOCdMwOl0cuSjjyjYuhVbTQ06k4lhkyYx6frr0bffLFy4bRv569fTUFam1NhGjmT8lVcSMXlyn7afbpzS8a++oqWuDkNICDFz5jB20SJXH19P79OBf/+bE5mZLPjDH9zxz2iNhNIA5YuhNGC1tkJ2tnJzrDcn96+pUaba7aEfaQhZM2Cab9/9xXe9XYR+8d/f/9fbRRh6OlYdaWjwbii1tSkzUw5xAyaU/r7q794ughjMgoOVmoq3tLYq4dhP9735sgETSlHhPQ/6EsItzOZv5zbqx4+/XerrlbnAu4wBGooGzJAAITzKz09Zl+18V849Fx0r6Z7FvYKDmYSSEB061nNrHzDYb2prlUCUphsgoSTEt3Q6GDFCWdm2o/biabW1ShAOG9Y/5xsAJJSEOFVgIERGgtXq+TXZGhuVBSmjorz7qZ+PkVAS4lQqlRJK4eFQXe25YGpsBJtNGZPk5ttvBroB8+mbEP1GrVZqL2q1si5bQIB7PxWrrVVqSDExSj+W6ERCSYieaDTKyrV+fsq6bE1NytJL57MEUmvrt31IUVFSQzoNCSUhTkethogI5VOx0lKlOefnp4TK2dyg2tr67Sd6ERFKp7b0IZ2WhJIQvTGbYfRopfO7okKp7Tidyqd1fn6g1Sp9UWq10ixzOJQgstmUPimdThmDFBoqH/v3gYSSEH2hViu3ogQFKZ3UDQ3KJP/NzUrTrn0CN1QqpRal1Sr9RWazEkQyUrvPJJSEOBsqlRIyJpPSDGtrU2pFTqdSQ1KrlVDS6fpv6e9BRkJJiPOh0Zxd/5LolYxTEkL4FAklIYRPkVASQvgUr/YpGTBQQok3izCgBRPc+05CDDBeCyUTJlJI8dbpe7VjW/vKD2GhJIxP6GVvIYS7eC2UdOgIIshbp++V3q6sbmpymHy6nEIMNtKnJITwKRJKQgifIqEkhPApEkpCCJ8ioSSE8CkSSkIInyKhJITwKRJKQgifIqEkhPApEkpCCJ8ioSSE8CkSSkIInyKhJITwKRJKQgifIqEkhPApEkpCCJ8ioSSE8CkSSkIInyKhJITwKRJKQgifIqEkhPApEkpCCJ8ioSSE8CkSSkIInyKhJITwKRJKQgifIqEkhPApEkpCCJ8ioSSE8CkSSkIInyKhJITwKRJKQgifIqEkhPApEkpCCJ8ioSSE8CkSSkIInyKhJITwKRJKQgifIqEkhPApEkpCCJ8ioSSE8CkSSkIInyKhJITwKRJKQgifIqEkhPApWm8XwCc4HNDUBM3Nrq/whgZoa8OiVkNBARgM4O//7XchhEeonE6n09uF8JqWFqipgaoqJZQcDlCrQadTvgM4ndDWBna78v9aLVgsEBysfFdLZVMIN1ozNGtKdjtUVsLJk2CzKbWfwMC+BYzdDrW1yvMtFoiIUL6rVJ4vtxBDwNCrKdXXQ0mJEixmM+j153YchwMaGqC1FcLDITJSqWEJIc7HEKspVVXB8eNKMyw09PxqN2o1BAQoTbuTJ5W+qKgopdYlhDhnQ6dDpKICCguV2kxQkPuaWxoNhIQoNbCCAqVvSghxzoZGKNXUKDUkvR6MRvcfX6VSOr6bm5Xga2lx/zmEGCIGfyg1NUFxMfj5eb5pFRQEjY1Kn5XD4dlzCTFIDe5QcjjgxAmlM9pk8vz5VCrlU7yKCqiu9vz5hBiEBncoWa1K57bF0n/n1GiUJmJpqTTjhDgHbvn0beezz1KSmdnpMf+AACxRUUy45hpCx44973N8fO+9jFmwgPFXXtm3JzgcUF6ujL7WaPp2jkceYcysWYyfP7/Hn/ti5yuvUHLwIJNmzyYhLEwZx3QKW10dnz7wAI62Nq765z9R97FsfSr/2V4jIXyQ24YEmCMjSb/zTtfPNquVoxs3suX3v+ein/2M8AkTzuv4KcuXEzB8eN+fUF+vfAUFnXaXo9u3U1NcTOoNNyjnWLyYgGHDzqucADq9nuLsbBIqK5WhB9pvL3PJ7t2odTocbW1ndcyj//d/1Bw7RuqKFafd56yvkRA+yG2hpNbpCI6L6/TYsEmTWP+zn3F0w4bzDqURaWln94SaGqWP5wyjtGuKizuf44ILzqVo3YTExnLyyBHqi4sxjxyp9DO1+yYjg9CEBMoOHDirY9YUFPS6z1lfIyF8kEcHT6q1WixRUTRWVroe+/iHP2TCNddw8tAhTh46xMJnnkGj03H43Xcp3rmTZqsVQ1AQUdOnk3jttajamzddmyZOh4PsDz+kcNs2bFYrhpAQRs+fT/yCBcqAxro6nH5+HPrvfzmemUlrYyOmsDDGzJpF7LRpbF29mor8fAAKd+1i3qpVbHvhhTM215wOB9kbNlC4eze2ujoMgYGMvugi4mfN6rSfv9lM0KhRHD94kAmTJrlCqdlqpeLIESZdf32nUDrjawG2PvkkFdnZSlm3bWPeb37Dtqee6nYd1//0p52vUVsbh955h+NffUVrQwOmYcMYs2ABsXPmnPd7K4SneHxEd2NFBcawMNfPKo2Ggi1bCI6LI/3OO9H6+bH3lVcoycwk/fbbCYqLoyovj8z//V/aWluZfNNNPR436/33yd+wgdRbbyV07FjKDx9m78svo9FqiZs+HVpa2L9xIycOHSJl8WLMw4ZRkZ/P/vffR2+xMPOOO9jy3HOYw8NJWbKkT307WZ99Rv62baRefz2hcXGU5+ayd80aNBoNcTNmuPZzOhyMnDyZgm3bmFBX53q8ZNcuAqOjMYSG9v21zJvHzJ/8hC1PPIE5MpKU5ctRa7U9Xseu9r/xBicyM0m55RbMw4dTkZ3N/tdfRx8URGRSUq+vVwhv8FgoNVut5K9fT11JCYnXXed6XK3R4HQ4SFm+HFA6fou2byfxuuuITE4GlGZIVV4exzZuZNL116PWdi6mvbmZ/PXriV+4kJFTpwIwasYMKvPyyP30U+LS0rA3NVG4axdJV19NZGIiAOawMGKnTXMdR6VSoVar0Wh7vwx2m438rVuJnzuXke2/0KPS0qgsLCR38+ZOoQQQlZzMobVrqSkoIGjMGNBqKd65k6hTzt+n1zJvnhJCHWVtv7+u63XsVt6mJgq3bCHp5ptd19UcESG1JOHz3BZKtceP8/4tt3R6zD8ggNTbbuvW13Hqp3G1xcU4HQ5C4uM77RM8ejS5n3xCfVkZlpEjO22rLyvDbrMRPn58p8fDxo7l2MaNtNTUUFtaisNuJ7DLc89VfUUF9pYWwseM6XzOuDiOffklLQ0N+J0yFsoQFETo6NEU79tH0Jw5NNXWUpmXx5S776aqvdnYp9dSV4dfQECPZTrTp5o1RUXK64+JOZeXK4TXuPXTt6n33OP62c9sRh8cjKqHe8xO/eW1t98r5tdlcKOu/XYQe3Nzt+fbrFZA6Wvpia22FrvNBuCqWZwvW3szbOvq1T1vr6/v9hqiUlI4sm4dE9vaKM7IIDQ+HkNICJwSSr2+ljOEUtfznarjump6aNYJ4cvc+ulbYHT02Reg/daPloaGTo+31NcDoOvh1hBt+3QjM3/60x7P6dfYiK19n5bGxrMuU4/lbJ9tcuYdd/RY+/LroZwjk5LY//bbVB89SsmuXURdeGH34/b2Ws5xJLrrurZfRyEGCq+P6A6Mjkal0VCVl9fp8ar8fLQGA6Yugw87nqPWaqkvLcU/IKDbl0qrJXDYMFQaDZXHjrmnnCNGKOcsL8ffZOr2peph6IGfXk9EfDxFGRlUFxQQ1d5ndFav5RxntgwcNUp5/Tk55/R8IbzF6/Mp+ZlMxMyaRe4nnxA4ahSBMTFUZGdTuHkzCQsX9vipmFavJ27ePLI++ABDcDDBY8Zgs1o59M476C0WUpcsQafXE5OeTs6mTZjDw7FERFB9/Dj73n2XlCVLGJWaik6vp+abb6grK8P/NE0k1zn9/Ym78EKy1q/HEBhIcEwMtro6Dq1bhz4gwDUAs5O2NqKSk8ncuJGw8ePx7+F2l15fS/tgSZ3RSE1REXUlJfifMu7pdHRGIzEXXUTOunWYIyOxjBxJ9dGj7HvtNVKWL2dUD7U2IXyB10MJIOnmm9EZDGS+9BItdXUYQkIYe8UVjF206LTPueDGG/EzGtn/xhvYamrQmUwMmzSJxMWLXXNsJ119NVp/f/a/9x6tzc0Yg4NJvOwyRqWmAjBm1ix2v/UWW55/nilLl/ZazguuuAI/g4H9H36IrbYWncHAsHHjSFy4sOcn2O0MT0pCtWVLt0/d+vxa2o255BJ2v/giW554gil33dVrWQGSvv99tHo9+19/ndbGRoxhYSRee60EkvBpA2Y63I9/+EPiL7uMcVdc0fvObW2Qna2M5vbmTJBVVTB8uPIlhOiLNV7vU+qNvbmZiiNHaG1sRH+G+9g60WiUUdQ9fHLXb5xO5as/pkwRYhDxiebbmZzIzCTzpZcISUhgRHp6359osShzZ3csm9TfmpqUWpqEkhBnZcA0386awwF5ecoSSr10YntERQWMGtVt6hIhxBn5fvPtnKnVytJHLS1KH1N/amxUaknBwf17XiEGgcEbSqD0K4WEKGu89Ze2NqXpFhmpzAsuhDgrgzuU1OpvF4nsMmLcI5xOZR6n0FCpJQlxjgZ3KIHSjIqKUhYP8PSabDU1Sv/ViBHe6VwXYhAYGr85QUFKp3Nzs9Lf425Op7J6iV6vnEeabUKcs6ERSqA0qWJjwW5XajTu+tDRbofKSjCbIS5Olu0W4jz5/DgltwoOVmoxJSXKaGuj8dxDxOFQFiaw25WP/Tv6roQQ52XwjlM6E7tdCaWTJ5UmncGgfPWlH6i1VWkC2u3KAM1hw5TvPcwbJYQ4a2uGVk2pg1arhElQkLJgZWWl8r1j9Hf7Db2A0sxra1NCyOlUnmuxKLUui0U6tIVws6FZU+rK4VBqTB1fTU3fBpFWqzT5DAalI1uvVxa4FEJ4whCtKXWlViv9S+1T8AohvEfaHkIInyKhJITwKRJKQgifogXWeLsQQgjRbsf/Ax8VzLcxuHOhAAAAAElFTkSuQmCC)

   ```python
   import datajoint as dj
   import math
   import numpy as np
   import datetime

   schema = dj.Schema('<your DataJointIO username>_shotput_experiment')

   @schema
   class Subject(dj.Manual):
       definition = """
       # Shot Put athlete subjects
       subject_id: int  # Unique identifier
       ---
       subject_name: varchar(50)  # Full name
       subject_launch_height: decimal(5, 2)  # [cm], Height of arm extension where weights become projectiles
       """

   @schema
   class Weight(dj.Lookup):
       definition = """
       # Available weights and their specification
       weight_mass: decimal(5, 2)  # [kg], Weight total mass
       ---
       weight_name: varchar(50)  # Weight name reference
       weight_density: decimal(5, 3)  # [g/cm^3], Weight density
       """
       # initial available weights
       contents = [(7.26, 'stainless steel', 8.024), (3.62, 'corundum', 4.),
                   (2.44, 'aluminium', 2.7)]

   @schema
   class Session(dj.Manual):
       definition = """
       # Experiment sessions where a shot put attempt is completed
       -> Subject
       session_date: datetime  # Date and time when a session took place
       ---
       -> Weight
       session_distance: decimal(4, 2)  # [m], x-axis displacement of the weight from the subject
       session_launch_split: time(3)  # Duration from when the attempt was initiated to when the weight was no longer in contact with the subject
       session_total_time: time(3)  # Duration from when the attempt was initiated to when the weight landed in the distance
       """

   @schema
   class ProjectileMetric(dj.Computed):
       definition = """
       # Calculated metrics from a session attempt
       -> Session
       ---
       projectilemetric_launch_velocity: decimal(5, 3)  # [m/s], Velocity at which the weight left the subject
       projectilemetric_work: decimal(6, 3)  # [N*m], Applied work to weight by subject in the attempt
       projectilemetric_attack_angle: decimal(4, 2) # [degrees], Angle of attack when the weight became a projectile
       """

       def make(self, key):
           g = 9.81  # [m/s^2], gravitational constant
           # retrieve and format known conditions
           session_knowns = (Session & key).fetch1(
               'session_distance', 'session_launch_split', 'session_total_time', 'weight_mass')
           d, taccel, t, m = [(float(d), tacel.total_seconds(),
                               round(t.total_seconds() - tacel.total_seconds(), 3), float(m))
                              for d, tacel, t, m in zip(*[[_] for _ in session_knowns])][0]
           y0 = float((Subject & key).fetch1('subject_launch_height'))/100.
           # angle of attack
           theta = math.degrees(math.atan((0.5 * g * t**2 - y0) / d))
           # projectile velocity
           v = d / t / math.cos(math.radians(theta))
           # total work on projectile (work-energy theorem)
           W = 0.5 * m * v**2

           self.insert1(dict(key, projectilemetric_launch_velocity=v, projectilemetric_work=W,
                             projectilemetric_attack_angle=theta))

   @schema
   class SimulatedSession(dj.Computed):
       definition = """
       # Simulated sessions for each available subject and weight
       -> Subject
       -> Weight
       ---
       simulatedsession_distance: decimal(4, 2)  # [m], Same as 'session_distance' above but simulated
       simulatedsession_launch_split: time(3)  # Average value of 'session_launch_split' above per subject over their sessions
       simulatedsession_total_time: time(3)  # Same as 'session_total_time' above but simulated
       simulatedsession_launch_velocity: decimal(5, 3)  # [m/s], Same as 'projectilemetric_launch_velocity' above but simulated
       simulatedsession_work: decimal(6, 3)  # [N*M], Average value of 'projectilemetric_work' above per subject over their sessions
       simulatedsession_attack_angle: decimal(4, 2)  # [degrees], Average value of 'projectilemetric_attack_angle' above per subject over their sessions
       """

       def make(self, key):
           g = 9.81  # [m/s^2], gravitational constant
           # retrieve and average metrics of subject based on prior sessions
           W, theta = [float(np.mean(_)) for _ in (ProjectileMetric & key).fetch(
               'projectilemetric_work', 'projectilemetric_attack_angle')]
           taccel_values = (Session & {k: v for k, v in key.items()
                                       if k != 'weight_mass'}).fetch('session_launch_split')
           taccel = (sum(taccel_values, datetime.timedelta(0)) / len(taccel_values)).total_seconds()
           y0 = float((Subject & key).fetch1('subject_launch_height'))/100.
           # retrive specs of weight
           m = float((Weight & key).fetch1('weight_mass'))
           # determine launch velocity
           v = (2 * W / m)**0.5
           # determine flight time
           t = [_ for _ in np.roots([-0.5*g, v * math.sin(math.radians(theta)), y0]) if _ > 0][0]
           # determine distance
           d = v * math.cos(math.radians(theta)) * t

           self.insert1(dict(key, simulatedsession_distance=d,
                             simulatedsession_launch_split=datetime.timedelta(seconds=taccel),
                             simulatedsession_total_time=datetime.timedelta(seconds=taccel + t),
                             simulatedsession_launch_velocity=v,
                             simulatedsession_work=W,
                             simulatedsession_attack_angle=theta))
   ```

   **Experiment Progress**: Let's suppose that the experiment is under way and the following are some points of interest:

   - Will Burns has a 189.23[cm] arm extension height
   - On 06/16/2021 08:20 AM, Will Burns launched a corundum weight for 8.93[m] in a session with a launch split of 1.25[s] for a total duration of 2.39[s]
   - A new weight was added (titanium alloy) with a mass of 4.03[kg] and a density of 4.45[g/cm^3]
   - John Smith has a 202[cm] arm extension height
   - On 06/16/2021 12:55 PM, John Smith launched a titanium alloy weight for 12.1[m] in a session with a launch split of 1.60[s] for a total duration of 3.2[s]

   **Question**: Judging from the simulated session data for both subjects, who can send stainless steel farther and by how much?
   
   **Hint**: It is not necessary to fully understand the algorithms in the `dj.Computed` tables as you will mainly be consuming their results.

## Bonus Questions (Not required). The following section will not be counted against you if unanswered or incorrect.

1. **REST**: How do you determine the REST verb for a route? How do you determine if arguments for a REST method should be in the body, header, or query parameters?

1. **OIDC**: How do you apply a permission model for a resource utilizing OIDC for authentication?

1. **NGINX/Certbot**: How would you define a route to allow certificate validation for a certbot behind an NGINX reverse proxy?

1. **Cryptography**: Explain GPG in 5 words or less.

1. **Web Frontend**: How can you achieve offline caching functionality for a PWA?

1. **Python**: Optimize the following Python code:

   ```python
   def gtv(d: dict):
      ret = None
      for k, v in d.items():
         if k == 'setting':
            ret = v
      return ret
   ```

1. **Python**: Solution must be a single, Python executable statement. How would you determine the current machine's MAC address?

1. **MATLAB**: Suppose you wanted to provide a flexible, dynamic, and indirect way to index into a MATLAB variable in a safe way (i.e. no `eval` use) since you cannot trust the index arguments. What is the most concise way to achieve this in accessing `2` from variable `s` below?

   ```matlab
   s = struct('settings', {3 struct('spec', [5;7;4;2])});
   ```

1. **MySQL**: Suppose you had an `order` table defined and populated as below. How would you optimize the following query so that it does not require a subquery?

   | day      | order_id | price | quantity |
   | -------- | -------- | ----- | -------- |
   | Monday   | 1        | 23.12 | 9        |
   | Tuesday  | 2        | 31.65 | 4        |
   | Monday   | 3        | 46.84 | 7        |
   | Tuesday  | 4        | 10.99 | 6        |

   ```sql
   SELECT t1.*
   FROM (
      SELECT `day`, SUM(price*quantity) as day_total
      FROM `order`
      GROUP BY `day`
   ) as t1
   WHERE t1.day_total > 300;
   ```

1. **Docker**: Being mindful of best security practices, what is a good approach to prevent privilege escalation when designing an image?

1. **Docker**: Which docker feature is most useful when needing to compile large codebases with high number of complex dependencies but it is only necessary to include the resultant binary in your assembled image?

1. **Bash**: On a typical ubuntu server, how would you read just the semantic version of a file (`./version.txt`)  with the following contents. Must be a single, executable BASH statement.

   ```text
   Awesome Tool: v4.8.2
   ```

1. **Kubernetes**: Say that you have some active deployments on a kubernetes cluster. If an `image:tag` involved in the deployment was recently republished to a docker registry (i.e. using the same tag), how would you ensure that your deployment uses the new one?

1. **Typescript**: What is a clear indication that proper best practices for static typing has not been followed in a codebase and could result in type unsafety?

1. **UTF-8**: What is the UTF-8 string that the following hex bytes represent?

   ```
   CE B7 D1 97 C2 A2 E2 84 AE
   ```

1. **GHA**: If you wanted to modify an action that is not maintained by GitHub for your own needs, how would you publish for your use?

1. **Jupyter**: What feature allows you to have multiple compute environments for jupyterhub users that can be simultaneously launched?

1. **Cloud/GH Pages**: If you had a domain registered with AWS or GCP, what steps would you take to enable a source committed in GitHub to be served on a custom subdomain using GitHub Pages?
