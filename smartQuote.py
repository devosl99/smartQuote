import sys
import os

inPath=sys.argv[1]
inPathNoExt=inPath[0:len(inPath)-4]
fileName=os.path.basename(os.path.normpath(inPath))
fileNameNoExt=os.path.basename(os.path.normpath(inPathNoExt))

os.makedirs("FITTED", exist_ok=True)
outPath="FITTED/"+fileNameNoExt+"_fit.txt"

print("Converting "+fileName+"...")

with open(inPath) as f:
	with open(outPath, 'w') as g:
		for line in f:
			newLine=line
			newLine=newLine.replace('“','\"')
			newLine=newLine.replace('”','\"')
			newLine=newLine.replace('‘','\'')
			newLine=newLine.replace('’','\'')
				
			g.write(newLine)

print("Done.")
