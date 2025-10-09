class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        ps = pt = 0

        while ps < ns and pt < nt:
            if s[ps] == t[pt]:
                ps += 1
            pt += 1

        return ps == ns
        
