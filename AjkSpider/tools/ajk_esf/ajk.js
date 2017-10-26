function captcha(token1) {
    var F = [];
    var v = 0;
    var D = "";
    var I = 8;
    function N(S) {
        return y(x(E(S), S.length * I))
    }
    function d(S) {
        return k(x(E(S), S.length * I))
    }
    function l(S) {
        return r(x(E(S), S.length * I))
    }
    function e(S, T) {
        return y(R(S, T))
    }
    function n(S, T) {
        return k(R(S, T))
    }
    function u(S, T) {
        return r(R(S, T))
    }
    function f() {
        return N("abc") == "900150983cd24fb0d6963f7d28e17f72"
    }
    F.push(["\x6D\x64\x35", "\x73\x68\x61\x31", "\x73\x68\x61\x32\x35\x36"]);
    function x(ac, X) {
        ac[X >> 5] |= 128 << ((X) % 32);
        ac[(((X + 64) >>> 9) << 4) + 14] = X;
        var ab = 1732584193;
        var aa = -271733879;
        var Z = -1732584194;
        var Y = 271733878;
        for (var U = 0; U < ac.length; U += 16) {
            var W = ab;
            var V = aa;
            var T = Z;
            var S = Y;
            ab = q(ab, aa, Z, Y, ac[U + 0], 7, -680876936);
            Y = q(Y, ab, aa, Z, ac[U + 1], 12, -389564586);
            Z = q(Z, Y, ab, aa, ac[U + 2], 17, 606105819);
            aa = q(aa, Z, Y, ab, ac[U + 3], 22, -1044525330);
            ab = q(ab, aa, Z, Y, ac[U + 4], 7, -176418897);
            Y = q(Y, ab, aa, Z, ac[U + 5], 12, 1200080426);
            Z = q(Z, Y, ab, aa, ac[U + 6], 17, -1473231341);
            aa = q(aa, Z, Y, ab, ac[U + 7], 22, -45705983);
            ab = q(ab, aa, Z, Y, ac[U + 8], 7, 1770035416);
            Y = q(Y, ab, aa, Z, ac[U + 9], 12, -1958414417);
            Z = q(Z, Y, ab, aa, ac[U + 10], 17, -42063);
            aa = q(aa, Z, Y, ab, ac[U + 11], 22, -1990404162);
            ab = q(ab, aa, Z, Y, ac[U + 12], 7, 1804603682);
            Y = q(Y, ab, aa, Z, ac[U + 13], 12, -40341101);
            Z = q(Z, Y, ab, aa, ac[U + 14], 17, -1502002290);
            aa = q(aa, Z, Y, ab, ac[U + 15], 22, 1236535329);
            ab = Q(ab, aa, Z, Y, ac[U + 1], 5, -165796510);
            Y = Q(Y, ab, aa, Z, ac[U + 6], 9, -1069501632);
            Z = Q(Z, Y, ab, aa, ac[U + 11], 14, 643717713);
            aa = Q(aa, Z, Y, ab, ac[U + 0], 20, -373897302);
            ab = Q(ab, aa, Z, Y, ac[U + 5], 5, -701558691);
            Y = Q(Y, ab, aa, Z, ac[U + 10], 9, 38016083);
            Z = Q(Z, Y, ab, aa, ac[U + 15], 14, -660478335);
            aa = Q(aa, Z, Y, ab, ac[U + 4], 20, -405537848);
            ab = Q(ab, aa, Z, Y, ac[U + 9], 5, 568446438);
            Y = Q(Y, ab, aa, Z, ac[U + 14], 9, -1019803690);
            Z = Q(Z, Y, ab, aa, ac[U + 3], 14, -187363961);
            aa = Q(aa, Z, Y, ab, ac[U + 8], 20, 1163531501);
            ab = Q(ab, aa, Z, Y, ac[U + 13], 5, -1444681467);
            Y = Q(Y, ab, aa, Z, ac[U + 2], 9, -51403784);
            Z = Q(Z, Y, ab, aa, ac[U + 7], 14, 1735328473);
            aa = Q(aa, Z, Y, ab, ac[U + 12], 20, -1926607734);
            ab = K(ab, aa, Z, Y, ac[U + 5], 4, -378558);
            Y = K(Y, ab, aa, Z, ac[U + 8], 11, -2022574463);
            Z = K(Z, Y, ab, aa, ac[U + 11], 16, 1839030562);
            aa = K(aa, Z, Y, ab, ac[U + 14], 23, -35309556);
            ab = K(ab, aa, Z, Y, ac[U + 1], 4, -1530992060);
            Y = K(Y, ab, aa, Z, ac[U + 4], 11, 1272893353);
            Z = K(Z, Y, ab, aa, ac[U + 7], 16, -155497632);
            aa = K(aa, Z, Y, ab, ac[U + 10], 23, -1094730640);
            ab = K(ab, aa, Z, Y, ac[U + 13], 4, 681279174);
            Y = K(Y, ab, aa, Z, ac[U + 0], 11, -358537222);
            Z = K(Z, Y, ab, aa, ac[U + 3], 16, -722521979);
            aa = K(aa, Z, Y, ab, ac[U + 6], 23, 76029189);
            ab = K(ab, aa, Z, Y, ac[U + 9], 4, -640364487);
            Y = K(Y, ab, aa, Z, ac[U + 12], 11, -421815835);
            Z = K(Z, Y, ab, aa, ac[U + 15], 16, 530742520);
            aa = K(aa, Z, Y, ab, ac[U + 2], 23, -995338651);
            ab = o(ab, aa, Z, Y, ac[U + 0], 6, -198630844);
            Y = o(Y, ab, aa, Z, ac[U + 7], 10, 1126891415);
            Z = o(Z, Y, ab, aa, ac[U + 14], 15, -1416354905);
            aa = o(aa, Z, Y, ab, ac[U + 5], 21, -57434055);
            ab = o(ab, aa, Z, Y, ac[U + 12], 6, 1700485571);
            Y = o(Y, ab, aa, Z, ac[U + 3], 10, -1894986606);
            Z = o(Z, Y, ab, aa, ac[U + 10], 15, -1051523);
            aa = o(aa, Z, Y, ab, ac[U + 1], 21, -2054922799);
            ab = o(ab, aa, Z, Y, ac[U + 8], 6, 1873313359);
            Y = o(Y, ab, aa, Z, ac[U + 15], 10, -30611744);
            Z = o(Z, Y, ab, aa, ac[U + 6], 15, -1560198380);
            aa = o(aa, Z, Y, ab, ac[U + 13], 21, 1309151649);
            ab = o(ab, aa, Z, Y, ac[U + 4], 6, -145523070);
            Y = o(Y, ab, aa, Z, ac[U + 11], 10, -1120210379);
            Z = o(Z, Y, ab, aa, ac[U + 2], 15, 718787259);
            aa = o(aa, Z, Y, ab, ac[U + 9], 21, -343485551);
            ab = s(ab, W);
            aa = s(aa, V);
            Z = s(Z, T);
            Y = s(Y, S)
        }
        return Array(ab, aa, Z, Y)
    }
    F.push(["\x6D\x64\x35", "\x73\x68\x61\x32\x35\x36", "\x73\x68\x61\x31"]);
    function m(X, U, T, S, W, V) {
        return s(g(s(s(U, X), s(S, V)), W), T)
    }
    function q(U, T, Y, X, S, W, V) {
        return m((T & Y) | ((~T) & X), U, T, S, W, V)
    }
    F.push(["\x73\x68\x61\x31", "\x6D\x64\x35", "\x73\x68\x61\x32\x35\x36"]);
    function Q(U, T, Y, X, S, W, V) {
        return m((T & X) | (Y & (~X)), U, T, S, W, V)
    }
    function K(U, T, Y, X, S, W, V) {
        return m(T ^ Y ^ X, U, T, S, W, V)
    }
    function o(U, T, Y, X, S, W, V) {
        return m(Y ^ (T | (~X)), U, T, S, W, V)
    }
    F.push(["\x73\x68\x61\x31", "\x73\x68\x61\x32\x35\x36", "\x6D\x64\x35"]);
    function R(U, X) {
        var W = E(U);
        if (W.length > 16) {
            W = x(W, U.length * I)
        }
        var S = Array(16),
        V = Array(16);
        for (var T = 0; T < 16; T++) {
            S[T] = W[T] ^ 909522486;
            V[T] = W[T] ^ 1549556828
        }
        var Y = x(S.concat(E(X)), 512 + X.length * I);
        return x(V.concat(Y), 512 + 128)
    }
    F.push(["\x73\x68\x61\x32\x35\x36", "\x6D\x64\x35", "\x73\x68\x61\x31"]);
    function s(S, V) {
        var U = (S & 65535) + (V & 65535);
        var T = (S >> 16) + (V >> 16) + (U >> 16);
        return (T << 16) | (U & 65535)
    }
    function g(S, T) {
        return (S << T) | (S >>> (32 - T))
    }
    F.push(["\x73\x68\x61\x32\x35\x36", "\x73\x68\x61\x31", "\x6D\x64\x35"]);
    function E(V) {
        var U = Array();
        var S = (1 << I) - 1;
        for (var T = 0; T < V.length * I; T += I) {
            U[T >> 5] |= (V.charCodeAt(T / I) & S) << (T % 32)
        }
        return U
    }
    function r(U) {
        var V = "";
        var S = (1 << I) - 1;
        for (var T = 0; T < U.length * 32; T += I) {
            V += String.fromCharCode((U[T >> 5] >>> (T % 32)) & S)
        }
        return V
    }
    function y(U) {
        var T = v ? "0123456789ABCDEF": "0123456789abcdef";
        var V = "";
        for (var S = 0; S < U.length * 4; S++) {
            V += T.charAt((U[S >> 2] >> ((S % 4) * 8 + 4)) & 15) + T.charAt((U[S >> 2] >> ((S % 4) * 8)) & 15)
        }
        return V
    }
    F.push(["\x6D\x64\x35", "\x73\x68\x61\x31"]);
    function k(V) {
        var U = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
        var X = "";
        for (var T = 0; T < V.length * 4; T += 3) {
            var W = (((V[T >> 2] >> 8 * (T % 4)) & 255) << 16) | (((V[T + 1 >> 2] >> 8 * ((T + 1) % 4)) & 255) << 8) | ((V[T + 2 >> 2] >> 8 * ((T + 2) % 4)) & 255);
            for (var S = 0; S < 4; S++) {
                if (T * 8 + S * 6 > V.length * 32) {
                    X += D
                } else {
                    X += U.charAt((W >> 6 * (3 - S)) & 63)
                }
            }
        }
        return X
    }
    F.push(["\x6D\x64\x35", "\x73\x68\x61\x32\x35\x36"]);
    var v = 0;
    var D = "";
    var I = 8;
    function t(S) {
        return j(p(H(S), S.length * I))
    }
    function L(S) {
        return P(p(H(S), S.length * I))
    }
    F.push(["\x73\x68\x61\x31", "\x6D\x64\x35"]);
    function h(S) {
        return b(p(H(S), S.length * I))
    }
    function M(S, T) {
        return j(C(S, T))
    }
    F.push(["\x73\x68\x61\x31", "\x73\x68\x61\x32\x35\x36"]);
    function z(S, T) {
        return P(C(S, T))
    }
    function O(S, T) {
        return b(C(S, T))
    }
    function G() {
        return t("abc") == "a9993e364706816aba3e25717850c26c9cd0d89d"
    }
    function p(af, Z) {
        af[Z >> 5] |= 128 << (24 - Z % 32);
        af[((Z + 64 >> 9) << 4) + 15] = Z;
        var ag = Array(80);
        var ae = 1732584193;
        var ad = -271733879;
        var ac = -1732584194;
        var ab = 271733878;
        var aa = -1009589776;
        for (var W = 0; W < af.length; W += 16) {
            var Y = ae;
            var X = ad;
            var V = ac;
            var U = ab;
            var S = aa;
            for (var T = 0; T < 80; T++) {
                if (T < 16) {
                    ag[T] = af[W + T]
                } else {
                    ag[T] = B(ag[T - 3] ^ ag[T - 8] ^ ag[T - 14] ^ ag[T - 16], 1)
                }
                var ah = s(s(B(ae, 5), a(T, ad, ac, ab)), s(s(aa, ag[T]), w(T)));
                aa = ab;
                ab = ac;
                ac = B(ad, 30);
                ad = ae;
                ae = ah
            }
            ae = s(ae, Y);
            ad = s(ad, X);
            ac = s(ac, V);
            ab = s(ab, U);
            aa = s(aa, S)
        }
        return Array(ae, ad, ac, ab, aa)
    }
    function a(T, S, V, U) {
        if (T < 20) {
            return (S & V) | ((~S) & U)
        }
        if (T < 40) {
            return S ^ V ^ U
        }
        if (T < 60) {
            return (S & V) | (S & U) | (V & U)
        }
        return S ^ V ^ U
    }
    function w(S) {
        return (S < 20) ? 1518500249 : (S < 40) ? 1859775393 : (S < 60) ? -1894007588 : -899497514
    }
    function C(U, X) {
        var W = H(U);
        if (W.length > 16) {
            W = p(W, U.length * I)
        }
        var S = Array(16),
        V = Array(16);
        for (var T = 0; T < 16; T++) {
            S[T] = W[T] ^ 909522486;
            V[T] = W[T] ^ 1549556828
        }
        var Y = p(S.concat(H(X)), 512 + X.length * I);
        return p(V.concat(Y), 512 + 160)
    }
    function s(S, V) {
        var U = (S & 65535) + (V & 65535);
        var T = (S >> 16) + (V >> 16) + (U >> 16);
        return (T << 16) | (U & 65535)
    }
    function B(S, T) {
        return (S << T) | (S >>> (32 - T))
    }
    F.push(["\x73\x68\x61\x32\x35\x36", "\x6D\x64\x35"]);
    function H(V) {
        var U = Array();
        var S = (1 << I) - 1;
        for (var T = 0; T < V.length * I; T += I) {
            U[T >> 5] |= (V.charCodeAt(T / I) & S) << (32 - I - T % 32)
        }
        return U
    }
    function b(U) {
        var V = "";
        var S = (1 << I) - 1;
        for (var T = 0; T < U.length * 32; T += I) {
            V += String.fromCharCode((U[T >> 5] >>> (32 - I - T % 32)) & S)
        }
        return V
    }
    function j(U) {
        var T = v ? "0123456789ABCDEF": "0123456789abcdef";
        var V = "";
        for (var S = 0; S < U.length * 4; S++) {
            V += T.charAt((U[S >> 2] >> ((3 - S % 4) * 8 + 4)) & 15) + T.charAt((U[S >> 2] >> ((3 - S % 4) * 8)) & 15)
        }
        return V
    }
    function P(V) {
        var U = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
        var X = "";
        for (var T = 0; T < V.length * 4; T += 3) {
            var W = (((V[T >> 2] >> 8 * (3 - T % 4)) & 255) << 16) | (((V[T + 1 >> 2] >> 8 * (3 - (T + 1) % 4)) & 255) << 8) | ((V[T + 2 >> 2] >> 8 * (3 - (T + 2) % 4)) & 255);
            for (var S = 0; S < 4; S++) {
                if (T * 8 + S * 6 > V.length * 32) {
                    X += D
                } else {
                    X += U.charAt((W >> 6 * (3 - S)) & 63)
                }
            }
        }
        return X
    }
    F.push(["\x73\x68\x61\x32\x35\x36", "\x73\x68\x61\x31"]);
    var c = function c(X) {
        function aq(at, ar) {
            return (at >>> ar) | (at << (32 - ar))
        }
        var al = Math.pow;
        var ab = al(2, 32);
        var V = "length";
        var aj, ai;
        var ad = "";
        var af = [];
        var U = X[V] * 8;
        var T = c.h = c.h || [];
        var ah = c.k = c.k || [];
        var Z = ah[V];
        var W = {};
        for (var Y = 2; Z < 64; Y++) {
            if (!W[Y]) {
                for (aj = 0; aj < 313; aj += Y) {
                    W[aj] = Y
                }
                T[Z] = (al(Y, 0.5) * ab) | 0;
                ah[Z++] = (al(Y, 1 / 3) * ab) | 0
            }
        }
        X += "\x80";
        while (X[V] % 64 - 56) {
            X += "\x00"
        }
        for (aj = 0; aj < X[V]; aj++) {
            ai = X.charCodeAt(aj);
            if (ai >> 8) {
                return
            }
            af[aj >> 2] |= ai << ((3 - aj) % 4) * 8
        }
        af[af[V]] = ((U / ab) | 0);
        af[af[V]] = (U);
        for (ai = 0; ai < af[V];) {
            var ae = af.slice(ai, ai += 16);
            var S = T;
            T = T.slice(0, 8);
            for (aj = 0; aj < 64; aj++) {
                var ag = aj + ai;
                var aa = ae[aj - 15],
                ac = ae[aj - 2];
                var an = T[0],
                ak = T[4];
                var ap = T[7] + (aq(ak, 6) ^ aq(ak, 11) ^ aq(ak, 25)) + ((ak & T[5]) ^ ((~ak) & T[6])) + ah[aj] + (ae[aj] = (aj < 16) ? ae[aj] : (ae[aj - 16] + (aq(aa, 7) ^ aq(aa, 18) ^ (aa >>> 3)) + ae[aj - 7] + (aq(ac, 17) ^ aq(ac, 19) ^ (ac >>> 10))) | 0);
                var ao = (aq(an, 2) ^ aq(an, 13) ^ aq(an, 22)) + ((an & T[1]) ^ (an & T[2]) ^ (T[1] & T[2]));
                T = [(ap + ao) | 0].concat(T);
                T[4] = (T[4] + ap) | 0
            }
            for (aj = 0; aj < 8; aj++) {
                T[aj] = (T[aj] + S[aj]) | 0
            }
        }
        for (aj = 0; aj < 8; aj++) {
            for (ai = 3; ai + 1; ai--) {
                var am = (T[aj] >> (ai * 8)) & 255;
                ad += ((am < 16) ? 0 : "") + am.toString(16)
            }
        }
        return ad
    };
    var A = {
        "\x6D\x64\x35": N,
        "\x73\x68\x61\x31": t,
        "\x73\x68\x61\x32\x35\x36": c
    };

    var X = token1;
    var ac = N(X);
    var U = 1;
    var Y = parseInt(ac.substring(0, U), 16);
    var W = F[Y % F.length];
    var ad = X;
    for (var aa = 0; aa < W.length; aa++) {
        var V = A[W[aa]];
        ad = V(ad)
    }
    return ad
}
