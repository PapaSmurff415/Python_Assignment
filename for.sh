#!/bin/bash

even_num=10

for ((i = 2; i <= even_num * 2; i += 2))
do
  printf "%d \n" $i
done
