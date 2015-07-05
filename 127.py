class Solution {
public:
    int n;
    vector<int> g[5010];
    bool vis[5010];
    int bfs(int st, int ed) {
        queue<pair<int,int> > Q;
        memset(vis, 0, sizeof(vis));
        Q.push(make_pair(st, 0));
        vis[st] = 1;
        
        while (!Q.empty()) {
            pair<int,int> t = Q.front();
            int u = t.first, step = t.second;
            if (u == ed) return step + 1;
            Q.pop();
            for (size_t i = 0;i < g[u].size(); ++i) {
                int v = g[u][i];
                if (vis[v]) continue;
                vis[v] = 1;
                Q.push(make_pair(v, step + 1));
            }
        }
        return 0;
    }
    int ladderLength(string start, string end, unordered_set<string> &dict) {
        map<string, int> mapper;
        unordered_set<string>::iterator itr;
        int id = 0, len = start.length();
        for (itr = dict.begin(); itr != dict.end(); ++itr) {
            string word = *itr;
            mapper[word] = id ++;
        }
        mapper[start] = id ++;  mapper[end] = id ++;
        n = id;
        for (int i = 0;i < n; ++i) g[i].clear();
        
        for (itr = dict.begin(); itr != dict.end(); ++itr) {
            string word = *itr;
            int u = mapper[word], v;
            for (int i = 0;i < len; ++i) {
                for (int j = 0;j < 26; ++j) {
                    if (word[i] - 'a' == j) continue;
                    string tmp = word;
                    tmp[i] = 'a' + j;
                    if (dict.find(tmp) == dict.end()) continue;
                    v = mapper[tmp];
                    g[u].push_back(v);
                }
            }
            int sdiff = 0, ediff = 0;
            for (int i = 0;i < len; ++i) {
                if (word[i] != start[i]) sdiff ++;
                if (word[i] != end[i]) ediff ++;
            }
            if (sdiff == 1) {
                g[n - 2].push_back(u);
                g[u].push_back(n - 2);
            }
            if (ediff == 1) {
                g[n - 1].push_back(u);
                g[u].push_back(n - 1);
            }
        }
        return bfs(n - 2, n - 1);
        
    }
};