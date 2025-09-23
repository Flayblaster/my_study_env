"""Escreva um programa que leia um número inteiro que representa uma quantidade de tempo em
segundos. Calcule e mostre na tela a quantidade de horas, minutos e segundos."""

segundos = int(input('Entrada(Segundos): '))
minutos = segundos//60
horas = minutos//60

segundos = segundos - (minutos*60)
minutos = minutos - (horas*60)

print(f'{horas}H / {minutos}Min / {segundos}Seg ')