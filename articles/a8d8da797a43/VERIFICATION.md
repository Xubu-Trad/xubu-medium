# Verification beside the article

Reviewed September 6, 2026. The article is preserved as published; these notes do not rewrite it.

## R2 proof: verified

Both complete hex fields match the verified evidence. Removing display line breaks gives exactly 2,884 characters in each. The source has SHA-256 `18f043170bc47a7d3aa9ee6989fe964803d240c90d62717b7fb7ad16539acd76`. Applying `R[j] = C[(320 + 641*j) mod 2884]` yields exactly the article's reordered hex. Its 1,442 decoded bytes have SHA-256 `2a77d034354b3ee698dd0266f93dfd5627e033cb8f79ec891498b80b7eab0e52`. The inverse and declared two-byte rotation pass.

## Displayed text: a whitespace difference

The published plaintext display contains the same words, spelling and punctuation, but is **1,434 bytes** when its rendered line boundaries are represented as LF. Compared with the exact 1,442-byte message, six blank-line LF bytes and two trailing spaces are missing. Its SHA-256 is `f65cdf78105f7679681a8c95aa07d407e915a3e47786e9b7d128c42628a679f5`.

The article's statement that its displayed plaintext preserves all spacing and line breaks exactly is therefore too strong. This is a presentation discrepancy; the two hex fields and their decoded result remain correct. A copied code field may also gain a final newline.

Use these separately supplied files for byte-exact verification:

- [01-source.hex](reproduction/01-source.hex)
- [02-reordered.hex](reproduction/02-reordered.hex)
- [03-message.txt](reproduction/03-message.txt)
- [decode_r2.py](reproduction/decode_r2.py)

Download the decoder beside `01-source.hex` and run `python decode_r2.py`. It checks both fingerprints and the complete inverse before writing the other two files. These supplemental files are the verified research artifacts; they are not labelled as downloads obtained from Medium.

## Interpretation and provenance

The known R1 chain reaches the manifesto, and the full supplied R2 cipher yields its development message. The evidence favors these as intended outputs; no further layer is established. That conclusion does not certify the impossibility of hidden content. [Endpoint assessment](https://github.com/Xubu-Trad/caw-lab/blob/canon/docs/ENDPOINT_ASSESSMENT.md).

The actual contract-creation account later linked the manifesto and development GitHub. The shared R1/R2 announcement account is a different address. Those verified roles support the project's manifesto connection without proving a common controller or identifying a person. [Primary transaction receipts](https://github.com/Xubu-Trad/caw-lab/blob/canon/docs/ONCHAIN_TRACE.md).

The reference to a red-herring warning needs its original channel kept clear: the raster image poem is separate from the exact IEND poem beginning `The archievest`. The latter does not contain that warning. The raster transcription remains qualified in the endpoint report. The new article's interpretation does not establish another cipher rule or a decoded warning that the manifesto is a decoy.

The liquidity and incentive statements are words inside the recovered message, not a fresh financial or contract audit. Personal experience and literary interpretation remain the author's account. This publication records the recovery; it is not independent confirmation by the original riddle-announcement account.

[Acquisition and fingerprints](preservation.json) · [Independent comparison](proof_check.json) · [Published decoding method](https://github.com/Xubu-Trad/caw-lab/blob/canon/layers/R2-020_hex_transposition/REPRODUCE.md)
