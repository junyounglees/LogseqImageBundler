# LogseqImageBundler

I wrote this script because logseq automatically imports any image files copied to your page into ../assets folder, but it seems impossible to export a page with bundled img files.

This script extracts the name of 'name.jpg' in your md or txt file, and searches jpg files starting with the names in your search directory, and copies the jpg files to your copy directory.

To-do
- [ ] code for changing the name of 'previousName.jpg'in the searched file into newly located jpg file.
- [ ] Supports for png and other img format. (Using img file type, not '.jpg' txt)