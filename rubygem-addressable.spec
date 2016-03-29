#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-addressable
Version  : 2.4.0
Release  : 8
URL      : https://rubygems.org/downloads/addressable-2.4.0.gem
Source0  : https://rubygems.org/downloads/addressable-2.4.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-coveralls
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support

%description
# Addressable
<dl>
<dt>Homepage</dt><dd><a href="https://github.com/sporkmonger/addressable">github.com/sporkmonger/addressable</a></dd>
<dt>Author</dt><dd><a href="mailto:bob@sporkmonger.com">Bob Aman</a></dd>
<dt>License</dt><dd>Apache 2.0</dd>
</dl>

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n addressable-2.4.0
gem spec %{SOURCE0} -l --ruby > rubygem-addressable.gemspec

%build
gem build rubygem-addressable.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
addressable-2.4.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/addressable-2.4.0
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/addressable-2.4.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/addressable.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/data/unicode.data
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/lib/addressable.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/lib/addressable/idna.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/lib/addressable/idna/native.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/lib/addressable/idna/pure.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/lib/addressable/template.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/lib/addressable/uri.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/lib/addressable/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/spec/addressable/idna_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/spec/addressable/net_http_compat_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/spec/addressable/rack_mount_compat_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/spec/addressable/security_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/spec/addressable/template_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/spec/addressable/uri_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/tasks/clobber.rake
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/tasks/gem.rake
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/tasks/git.rake
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/tasks/metrics.rake
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/tasks/rspec.rake
/usr/lib64/ruby/gems/2.3.0/gems/addressable-2.4.0/tasks/yard.rake
/usr/lib64/ruby/gems/2.3.0/specifications/addressable-2.4.0.gemspec
