#wahtzdis

## Description
Archaeologists have discovered a new script while exploring the ruins of an alien colony. But with all the 1337 archaeologists dead, only n00b can find out the what this[http://hack.bckdr.in/WAHTZDIS] means.

Created by: Ashish Chaudhary
No. of Correct Submissions: 405

## Solution
The webste gives us a wall of gibberish. With a bit of googling we can find out that this is javascript encoded with JSFuck (http://esolangs.org/wiki/JSFuck).

Simply run it in the console and we get this output
```
ƒ anonymous() {
alert('window.atob("eTB1X3czcjNfbHVja3lfN2gxNV83MW0zX24wMGI=")')
}
```
The atob function reveals that this is encoded with base64, so lets decode it.

```
$ echo -n eTB1X3czcjNfbHVja3lf -dxNV83MW0zX24wMGI= | base64
```

And the output is our flag. Generate the sha256sum and get your reward :)
