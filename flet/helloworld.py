#!/usr/bin/python3
"""helloworld app"""
import flet as ft

def main(page: ft.Page):
    page.title = "Hello"

    text = ft.Text(value="HelloWorld!")

    page.controls.append(text)

    page.update()

ft.app(target=main)