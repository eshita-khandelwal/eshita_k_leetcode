/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf4);
 */

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        
        int copiedchars=0,readchars=4;
        while(copiedchars<n && readchars==4)
        {
            readchars=read4(buf+copiedchars);
            copiedchars+=readchars;
        }
        return min(n,copiedchars);
        //return n;
    }
};