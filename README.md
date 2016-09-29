vim-rplugin
===============================================================================
[![Travis CI](https://img.shields.io/travis/lambdalisue/vim-rplugin/master.svg?style=flat-square&label=Travis%20CI)](https://travis-ci.org/lambdalisue/vim-rplugin)
[![AppVeyor](https://img.shields.io/appveyor/ci/lambdalisue/vim-rplugin/master.svg?style=flat-square&label=AppVeyor)](https://ci.appveyor.com/project/lambdalisue/vim-rplugin/branch/master)
![Version 0.1.0](https://img.shields.io/badge/version-0.1.0-yellow.svg?style=flat-square)
![Support Vim 8.0 or above](https://img.shields.io/badge/support-Vim%208.0%20or%20above-yellowgreen.svg?style=flat-square)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE.md)
[![Doc](https://img.shields.io/badge/doc-%3Ah%20rplugin-orange.svg?style=flat-square)](doc/rplugin.txt)

A library to support Vim 8 for plugin which is written with Python 3 remote plugin of Neovim.
Inspired by [Shougo/denite.nvim](https://github.com/lambdalisue/denite.nvim).

**Note: This is an alpha version.**

Install
-------------------------------------------------------------------------------
```vim
Plug 'lambdalisue/vim-rplugin'
```

Usage
-------------------------------------------------------------------------------
1. Use `rplugin.Neovim` class to wrap `vim` module.
2. Call `rplugin#init({runtimepath})` to add `{runtimepath}/rplugin/python3` to `sys.path`

Wrapping `vim` module with `rplugin.Neovim` will

- Add `vim.call(name, *args)` interface
- Add `vim.funcs.{fname}(*args)` interface
- Returns `str` instead of `bytes` in Python 3

You can see a demo project at http://github.com/lambdalisue/vim-rplugin-test

Plugins which use vim-rplugin to support Vim 8
-------------------------------------------------------------------------------

- [lambdalisue/prompt.nvim](https://github.com/lambdalisue/prompt.nvim)
- [lambdalisue/lista.nvim](https://github.com/lambdalisue/lista.nvim)

