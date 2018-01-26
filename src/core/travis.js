import IsNil from 'lodash-es/isNil';
import Process from 'process';


export class Travis {
    get branch() {
        let branch = Process.env['TRAVIS_BRANCH'] || null;

        if(IsNil(branch) || branch === this.tag) {
            return null;
        }

        return branch;
    }

    get build_number() {
        return Process.env['TRAVIS_BUILD_NUMBER'] || null;
    }

    get tag() {
        return Process.env['TRAVIS_TAG'] || null;
    }
}

export default new Travis();
