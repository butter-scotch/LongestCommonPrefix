class Solution:
  def longestCommonPrefix(self, strs):

    pre = ""
    i = 0
    
    if len(strs) == 0:
      return pre
    elif len(strs) == 1:
      pre += strs[0]
      return pre
    else:
      for i in range(min([len(x) for x in strs])):
        if [strs[x][i] for x in range(len(strs))].count(strs[0][i]) == len(strs):
          pre += strs[0][i]
          i += 1
        else:
          return pre
      return pre


result = Solution()
print(result.longestCommonPrefix(["flower", "flow", "flight"]))

# output "fl"


# 最初の文字からリスト内の単語のうちの最小文字数まで調べる
# i <= min([len(x) for x in strs])-1

# リストが空ではない場合
# len(strs) != 0

# 一文字目が全て同じかどうかを判定
# [strs[x][0] for x in range(len(strs))].count(strs[0][0]) == len(strs)


