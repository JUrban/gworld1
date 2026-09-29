// Bounded valid-coloring graph in B3, targeting the remaining B4 sector.
// Uses the separately pinned CBraid canonical forms; findings need replay.
#include "braiding.h"
#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <unordered_set>
#include <vector>

using W=std::vector<int>;
using C=std::array<W,3>;
const size_t WORD_CAP=20000;
const int RANK_CAP=20;
long caps=0, divisions=0, division_fails=0;
int rankof(const W& w) { int n=2; for(int j:w)n=std::max(n,std::abs(j)+1);return n; }
int eps(const W& w) {int e=0;for(int j:w)e+=j>0?1:-1;return e;}
void append(W& a,const W& b) {for(int j:b) {if(!a.empty()&&a.back()==-j)a.pop_back();else a.push_back(j);}}
W inv(const W& w) {W r;for(auto i=w.rbegin();i!=w.rend();++i)r.push_back(-*i);return r;}
W shift(const W& w) {W r;for(int j:w)r.push_back(j>0?j+1:j-1);return r;}
CBraid::ArtinBraid braid(const W& w,int n) {
    std::list<CBraid::sint16> letters(w.begin(),w.end());
    auto b=Braiding::WordToBraid(letters,n);b.MakeLCF();return b;
}
bool equal(const W& a,const W& b) {
    if(a==b)return true;
    int n=std::max(rankof(a),rankof(b));
    return braid(a,n)==braid(b,n);
}
std::string key(const W& w,int n) {std::ostringstream s;s<<braid(w,n);return s.str();}
W shelf(const W& a,const W& b) {W r=a;append(r,shift(b));append(r,{1});append(r,inv(shift(a)));return r;}
bool delete_strand(const W& w,int start,W& out) {
    int pos=start;out.clear();
    for(int j:w) {
        int i=std::abs(j);
        if(pos==i)pos=i+1;
        else if(pos==i+1)pos=i;
        else {int k=i-(pos<i?1:0);append(out,{j>0?k:-k});}
    }
    return pos==start;
}
W compact(W w) {
    W r;append(r,w);w=r;
    int n=rankof(w);
    while(n>2) {
        if(!delete_strand(w,n,r)||!equal(w,r))break;
        w=r;--n;
    }
    if(equal(w,{}))return {};
    return w;
}
bool admissible(const W& w) {return w.size()<=WORD_CAP&&rankof(w)<=RANK_CAP;}
bool step(C& color,int j) {
    int i=std::abs(j)-1;
    W a=color[i],c=color[i+1],d;
    if(j>0) {
        d=shelf(a,c);
        if(!admissible(d)){++caps;return false;}
        color[i]=compact(d);color[i+1]=a;return true;
    }
    ++divisions;
    if(eps(a)==0){++division_fails;return false;}
    // Solve c shelf d=a, using S(d)=c^-1 a S(c) s1^-1.
    W w=inv(c);append(w,a);append(w,shift(c));append(w,{-1});
    if(!admissible(w)){++caps;return false;}
    if(!delete_strand(w,1,d)||!equal(w,shift(d))) {
        ++division_fails;return false;
    }
    d=compact(d);
    if(eps(d)<0||!equal(shelf(c,d),a))throw std::runtime_error("Division certificate");
    color[i]=c;color[i+1]=d;return true;
}
void jsonword(std::ostream& s,const W& w) {
    s<<"[";for(size_t i=0;i<w.size();++i){if(i)s<<",";s<<w[i];}s<<"]";
}
struct State {W word;C color;};
int main(int argc,char** argv) {
    if(argc!=4)return 2;
    int depth=std::stoi(argv[1]);size_t statecap=std::stoul(argv[2]);
    {std::ifstream exists(argv[3]);if(exists.good())return 3;}
    // Exact inverse steps and Artin relations, including a negative control.
    C unit{}; C positive=unit;
    if(!step(positive,1)||!step(positive,-1)||positive!=unit)return 4;
    C bad=unit;if(step(bad,-1))return 5;
    C left=unit,right=unit;
    for(int j:{1,2,1})if(!step(left,j))return 6;
    for(int j:{2,1,2})if(!step(right,j))return 7;
    for(int i=0;i<3;++i)if(!equal(left[i],right[i]))return 8;
    std::vector<W> representatives={{},{2},{1,2},{1,1,-2}};
    std::unordered_set<std::string> known;
    for(W a:representatives){W b=a;append(b,{2,1});append(b,inv(shift(a)));known.insert(key(b,4));}
    if(known.size()!=4)return 9;
    std::unordered_set<std::string> seen{key({},3)};
    std::vector<State> level{{{},unit}};
    std::ofstream out(argv[3]);out<<"{\"depth_cap\":"<<depth<<",\"state_cap\":"<<statecap
        <<",\"word_cap\":"<<WORD_CAP<<",\"rank_cap\":"<<RANK_CAP<<",\"novel_hits\":[";
    std::ofstream profile(std::string(argv[3])+".states.jsonl");
    long hits=0,ends=0,positive_count=0,extra_cone_count=0,outside_count=0;
    int completed=0;bool stopped=false;
    for(int dep=0;dep<=depth;++dep) {
        std::vector<State> next;
        for(const State& st:level) {
            bool positive=braid(st.word,3).LeftDelta>=0;
            W shifted=inv({1,1,-2});append(shifted,st.word);
            bool extra=braid(shifted,3).LeftDelta>=0;
            if(positive)++positive_count;
            else if(extra)++extra_cone_count;
            else {
                ++outside_count;
                if(outside_count<=10) {
                    std::cout<<"OUTSIDE_TWO_CONES depth "<<dep<<" word ";
                    jsonword(std::cout,st.word);std::cout<<std::endl;
                }
            }
            profile<<"{\"path\":";jsonword(profile,st.word);
            profile<<",\"positive\":"<<(positive?"true":"false")
                   <<",\"extra_cone\":"<<(extra?"true":"false")<<",\"colors\":[";
            for(int i=0;i<3;++i){if(i)profile<<",";jsonword(profile,st.color[i]);}
            profile<<"]}\n";
            if(st.color[2].empty()) {
                ++ends;
                W b=st.word;append(b,{2,1});append(b,inv(shift(st.word)));
                if(known.insert(key(b,4)).second) {
                    if(hits++)out<<",";
                    out<<"{\"depth\":"<<dep<<",\"path\":";jsonword(out,st.word);
                    out<<",\"a\":";jsonword(out,st.color[0]);
                    out<<",\"c\":";jsonword(out,st.color[1]);
                    out<<",\"braid\":";jsonword(out,b);out<<"}";out.flush();
                    std::cout<<"NEW_COSET depth "<<dep<<" word ";jsonword(std::cout,st.word);std::cout<<std::endl;
                }
            }
            if(dep==depth)continue;
            for(int j:{1,2,-1,-2}) {
                W w=st.word;append(w,{j});auto k=key(w,3);
                if(seen.count(k))continue;
                C c=st.color;
                if(!step(c,j))continue;
                seen.insert(k);next.push_back({w,c});
                if(seen.size()>=statecap){stopped=true;break;}
            }
            if(stopped)break;
        }
        std::cout<<"depth "<<dep<<" layer "<<level.size()<<" total "<<seen.size()
            <<" endpoints "<<ends<<" new_cosets "<<hits<<" cap_skips "<<caps<<std::endl;
        if(stopped)break;
        completed=dep;level.swap(next);
        if(level.empty())break;
    }
    out<<"],\"completed_depth\":"<<completed<<",\"states\":"<<seen.size()
        <<",\"endpoints\":"<<ends<<",\"new_cosets\":"<<hits
        <<",\"cap_skips\":"<<caps<<",\"division_attempts\":"<<divisions
        <<",\"division_failures\":"<<division_fails<<",\"state_cap_hit\":"<<(stopped?"true":"false")
        <<",\"positive_states\":"<<positive_count<<",\"extra_cone_only\":"<<extra_cone_count
        <<",\"outside_two_cones\":"<<outside_count
        <<",\"scope\":\"Bounded reachable valid-coloring graph only; no exhaustion of special braids or cosets.\"}\n";
    std::cout<<"PASS bounded B9 coloring-coset probe"<<std::endl;
}
