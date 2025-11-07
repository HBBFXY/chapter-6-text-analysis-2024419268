# -*- coding: utf-8 -*-
# 在此文件处编辑代码
def analyze_text_frequency(text):
     text = text.replace(" ", "").replace("\n", "").replace("\t", "")
     frequency = {}
     for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

     sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

     for char, count in sorted_frequency:
        print(f"'{char}': {count}")

input_text = input("请输入一段文本：")
analyze_text_frequency(input_text)
