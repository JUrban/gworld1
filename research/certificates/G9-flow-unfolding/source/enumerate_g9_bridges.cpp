// Independent rank-two enumeration of strict bridge flows.
// A key consists of sorted (x+64,y+64,axis,coefficient+64) bytes for
// nonzero positively oriented lattice edges. No Python code is used.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>

using Edge=std::array<int,3>;
int bound;
std::map<Edge,int> current_flow;
std::vector<std::unordered_map<std::string,unsigned char>> known;
std::vector<std::vector<std::uint64_t>> counts;
std::vector<std::uint64_t> irreducible_counts;
std::uint64_t half_words=0,bridge_words=0;

void add_edge(const Edge& e,int change){
    auto i=current_flow.find(e);
    if(i==current_flow.end()){current_flow.emplace(e,change);return;}
    i->second+=change;if(i->second==0)current_flow.erase(i);
}

void visit(int x,int y,int maxheight,int depth,int last){
    if(depth){
        ++half_words;
        if(x==maxheight){
            ++bridge_words;
            std::string key;key.reserve(4*current_flow.size());
            for(const auto& pair:current_flow){
                key.push_back(char(pair.first[0]+64));
                key.push_back(char(pair.first[1]+64));
                key.push_back(char(pair.first[2]));
                key.push_back(char(pair.second+64));
            }
            auto [it,inserted]=known[x].emplace(std::move(key),depth);
            if(inserted){
                ++counts[x][depth];
                std::vector<int> crossings(x,0);
                for(const auto& edge:current_flow)
                    if(edge.first[2]==0 && edge.first[0]>0 && edge.first[0]<x)
                        ++crossings[edge.first[0]];
                bool atom=true;
                for(int h=1;h<x;++h)if(crossings[h]==1)atom=false;
                if(atom){++irreducible_counts[depth];it->second|=128;}
            }else{
                int olddepth=it->second&127;bool atom=(it->second&128)!=0;
                if(depth<olddepth){
                    --counts[x][olddepth];++counts[x][depth];
                    if(atom){--irreducible_counts[olddepth];++irreducible_counts[depth];}
                    it->second=depth|(atom?128:0);
                }
            }
        }
    }
    if(depth==bound)return;
    for(int letter:{1,-1,2,-2}){
        if(letter==-last)continue;
        int nx=x,ny=y,axis=std::abs(letter)-1,sgn=letter>0?1:-1;
        if(axis==0)nx+=sgn;else ny+=sgn;
        if(nx<=0)continue;
        Edge e={sgn>0?x:nx,sgn>0?y:ny,axis};
        add_edge(e,sgn);
        visit(nx,ny,std::max(maxheight,nx),depth+1,letter);
        add_edge(e,-sgn);
    }
}

int main(int argc,char**argv){
    if(argc!=2){std::cerr<<"Usage: enumerate_g9_bridges MAX_LENGTH\n";return 2;}
    bound=std::atoi(argv[1]);
    if(bound<1||bound>30){std::cerr<<"Supported length 1..30\n";return 2;}
    known.resize(bound+1);counts.assign(bound+1,std::vector<std::uint64_t>(bound+1,0));
    irreducible_counts.assign(bound+1,0);
    visit(0,0,0,0,0);
    if(!current_flow.empty()){std::cerr<<"Backtracking failed\n";return 1;}
    std::cout<<"{\"rank\":2,\"max_length\":"<<bound<<",\"halfspace_words\":"<<half_words
             <<",\"bridge_words\":"<<bridge_words<<",\"counts_by_height\":[";
    for(int h=1;h<=bound;++h){
        if(h>1)std::cout<<',';
        std::cout<<"{\"height\":"<<h<<",\"distinct_flows\":"<<known[h].size()<<",\"counts\":[";
        for(int n=0;n<=bound;++n){if(n)std::cout<<',';std::cout<<counts[h][n];}
        std::cout<<"]}";
    }
    std::cout<<"],\"irreducible_counts\":[";
    for(int n=0;n<=bound;++n){if(n)std::cout<<',';std::cout<<irreducible_counts[n];}
    std::cout<<"]}\nPASS G9 INDEPENDENT BRIDGE ENUMERATION\n";
}
