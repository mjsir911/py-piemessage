"Dynamic Variables
let owen = "Owen Davies"
let name = "Marco Sirabella"
let nVars = {
 \"appname" : "pymessage", 
 \"author" : name . ", " . owen,
 \"copyright" : "", 
 \"credits" : name . ", " . owen,
 \"license" : "new BSD 3-Clause", 
 \"version" : "0.0.3", 
 \"maintainers" : name . ", " . owen,
 \"email" : 'msirabel@gmail.com, dabmancer@dread.life', 
 \"status" : "Prototype", 
 \"module" : ""}

let uVars = copy(nVars)

unlet uVars.credits
unlet uVars.author
"unlet dVars.credits
unlet uVars.maintainers

"__smail__      =il.com"
"__email__
 "\"credits" : credlist, 

augroup Skeletons
 autocmd BufNewFile,BufRead *.py call g:VarLoop(uVars)
 autocmd BufNewFile *.py call g:VarLoop(nVars)
augroup END
fun g:VarLoop(list)
 try
  for var in keys(a:list)
   call PythonMetaUpdate(var, a:list[var])
  endfor
  catch
 endtry
endfunction
