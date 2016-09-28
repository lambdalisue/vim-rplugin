vim-rplugin
===============================================================================
![Version 1.0.0](https://img.shields.io/badge/version-1.0.0-yellow.svg?style=flat-square)
![Support Vim 8.0 or above](https://img.shields.io/badge/support-Vim%208.0%20or%20above-yellowgreen.svg?style=flat-square)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE.md)
[![Doc](https://img.shields.io/badge/doc-%3Ah%20lista-orange.svg?style=flat-square)](doc/rplugin.txt)

A library to support Neovim/Vim8 compatible remote plugin.
Inspired by [Shougo/denite.nvim](https://github.com/lambdalisue/denite.nvim).

Install
-------------------------------------------------------------------------------

```vim
Plug 'lambdalisue/vim-rplugin'
```

Plugins which use vim-rplugin to support Vim 8
-------------------------------------------------------------------------------

- [lambdalisue/lista.nvim](https://github.com/lambdalisue/lista.nvim)


Usage
-------------------------------------------------------------------------------

Wrap `vim` instance with a `rplugin.Neovim` proxy class to 

- Adds `vim.call(name, *args)` interface
- Returns str instead of bytes in Python 3
- Returns '\udc80' instead of b'\x80' for special key in `getchar()` function

You can see a demo project at http://github.com/lambdalisue/vim-rplugin-test
