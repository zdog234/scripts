echo off
start "C:\Program Files (x86)\Atlassian\SourceTree\SourceTree.exe"  -ArgumentList "-f $((Resolve-Path $args[0]).toString())"