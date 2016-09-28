let s:sep = (!has('win32') && !has('win64')) || &shellslash ? '/' : '\\'


function! rplugin#init(runtimepath, ...) abort
  let options = extend({
        \ 'python': has('python'),
        \ 'python3': has('python3'),
        \}, get(a:000, 0, {})
        \)
  let lib2 = join([a:runtimepath, 'rplugin', 'python'], s:sep)
  let lib3 = join([a:runtimepath, 'rplugin', 'python3'], s:sep)
  let result = {
        \ 'python': 0,
        \ 'python3': 0,
        \}

  if options.python && isdirectory(lib2)
    try
      python << EOC
import sys
import vim
sys.path.insert(0, vim.eval('lib2'))
EOC
      let result.python = 1
    catch
      echoerr v:exception
    endtry
  endif

  if options.python3 && isdirectory(lib3)
    try
      python3 << EOC
import sys
import vim
sys.path.insert(0, vim.eval('lib3'))
EOC
      let result.python3 = 1
    catch
      echoerr v:exception
    endtry
  endif

  return result
endfunction
